import sys


from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QApplication,
                             QWidget,
                             QPushButton,
                             QFileDialog,
                             QMessageBox,
                             QVBoxLayout,
                             QHBoxLayout,
                             QLabel)


from ImageIterator import ImageIterator


class MyWindow(QWidget):

    def __init__(self):
        '''
        Initialize the main window.
        '''
        super().__init__()

        self.iterator = None
        self.path = None

        self.init_ui()

    def init_ui(self) -> None:
        '''
        Set up the interface.
        '''

        self.setGeometry(100, 100, 700, 500)
        self.setFixedSize(700, 500)
        self.setWindowTitle('MyWindow')

        self.open_btn = QPushButton('Open csv-file', self)
        # self.open_btn.resize(self.open_btn.sizeHint())
        self.open_btn.move(50, 460)
        self.open_btn.clicked.connect(self.open_csv)

        self.next_btn = QPushButton('Next img', self)
        self.next_btn.setEnabled(False)
        # self.next_btn.resize(self.next_btn.sizeHint())
        self.next_btn.move(600, 460)
        self.next_btn.clicked.connect(self.show_next_img)

        self.image_label = QLabel("Open dataset.", self)
        # self.image_label.move(50, 50)
        self.layout = QVBoxLayout()
        self.image_label.setScaledContents(True)
        self.layout.addWidget(self.image_label)

        hbox = QHBoxLayout()
        # hbox.addStretch(1)
        hbox.addWidget(self.open_btn)
        hbox.addWidget(self.next_btn)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(self.layout)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

    def open_csv(self) -> None:
        '''
        Open a file dialog to select an annotation file.
        '''
        fname = QFileDialog.getOpenFileName(self,
                                            'Open file',
                                            '/ann',
                                            'CSV Files (*.csv)')[0]
        if fname:
            try:
                self.iterator = ImageIterator(fname)
                self.next_btn.setEnabled(True)
                self.show_next_img()
            except Exception as e:
                QMessageBox.critical(self, f"Error: {str(e)}")

    def show_next_img(self) -> None:
        '''
        Display the next image in the dataset.
        '''
        if self.iterator:
            try:
                self.path = next(self.iterator)
                pixmap = QPixmap(self.path)
                if pixmap.isNull():
                    raise ValueError("Image couldn't be uploaded.")
                self.image_label.setPixmap(pixmap)

            except StopIteration:
                reply = QMessageBox.question(self,
                                             "End",
                                             "The images are over \n Load new annotation file?",
                                             QMessageBox.Yes | QMessageBox.No,
                                             QMessageBox.No)
                if reply == QMessageBox.Yes:
                    self.open_csv()
                else:
                    self.image_label.setText("Open dataset.")
                    self.next_btn.setEnabled(False)

            except Exception as e:
                QMessageBox.critical(self,
                                     "Error",
                                     f"Something went wrong: {str(e)}")


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyWindow()
    ex.show()
    sys.exit(app.exec_())
