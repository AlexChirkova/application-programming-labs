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
        self.open_btn.move(50, 460)
        self.open_btn.clicked.connect(self.open_csv)

        self.next_btn = QPushButton('Next img', self)
        self.next_btn.setEnabled(False)
        self.next_btn.move(600, 460)
        self.next_btn.clicked.connect(self.show_next_img)

        self.image_label = QLabel("Open dataset.", self)
        self.layout = QVBoxLayout()
        self.image_label.setScaledContents(True)
        self.layout.addWidget(self.image_label)

        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.open_btn)
        self.hbox.addWidget(self.next_btn)

        self.vbox = QVBoxLayout()
        self.vbox.addStretch(1)
        self.vbox.addLayout(self.layout)
        self.vbox.addLayout(self.hbox)

        self.setLayout(self.vbox)

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
                QMessageBox.critical(self, "Error", f"Error: {str(e)}")

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
                                             "The images are over \n Do you want to load new annotation file?",
                                             QMessageBox.Yes | QMessageBox.No,
                                             QMessageBox.No)
                if reply == QMessageBox.Yes:
                    self.open_csv()
                else:
                    self.image_label.setText("Open dataset.")
                    self.next_btn.setEnabled(False)

            except ValueError:
                is_next = QMessageBox.information(self,
                                                  "Error",
                                                  "Path is incorrect")
                self.image_label.setText("Press \"Next img\" to continue viewing.")

            except Exception as e:
                QMessageBox.critical(self,
                                     "Error",
                                     f"Something went wrong: {str(e)}")


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyWindow()
    ex.show()
    sys.exit(app.exec_())
