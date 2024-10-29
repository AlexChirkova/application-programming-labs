import cv2 as cv
import numpy as np


from matplotlib import pyplot as plt


def create_hist_rgb(image: np.ndarray) -> tuple:
    red_hist = cv.calcHist(image, [2], None, [256], [0, 256])
    green_hist = cv.calcHist(image, [1], None, [256], [0, 256])
    blue_hist = cv.calcHist(image, [0], None, [256], [0, 256])
    return red_hist, green_hist, blue_hist


def show_hist_rgb(hist: tuple) -> None:
    plt.figure(figsize=(10, 5))
    plt.title('Histogram')
    plt.xlabel('Pixel range')
    plt.ylabel('Pixels\' count')
    plt.grid(color='gray', linestyle='--', linewidth=0.5)

    plt.plot(hist[0])
    plt.plot(hist[1])
    plt.plot(hist[2])
    plt.show()


def reflection(img: np.ndarray, axis: int) -> np.ndarray:
    return cv.flip(img, axis)
