import cv2
import os
import pandas as pd
import matplotlib.pyplot as plt


def create_df(annotation_file: str) -> pd.DataFrame:
    return pd.read_csv(annotation_file)


def add_h_w_d(df: pd.DataFrame, path_to_images: str) -> None:
    h = []
    w = []
    d = []
    for i in os.listdir(path_to_images):
        img = os.path.join(path_to_images, i)
        h.append(cv2.imread(img).shape[0])
        w.append(cv2.imread(img).shape[1])
        d.append(cv2.imread(img).shape[2])

    df.insert(2, "Height", pd.Series(h), True)
    df.insert(3, "Width", pd.Series(w), True)
    df.insert(4, "Depth", pd.Series(d), True)


def statistical_information(df: pd.DataFrame) -> pd.DataFrame:
    return df.loc[:, ("Height", "Width", "Depth")].agg(["min", "max", "mean"])


def sort_df_by_hw(df: pd.DataFrame, max_height: float, max_width: float) -> pd.DataFrame:
    return df[(df["Height"] < max_height) & (df["Width"] < max_width)]


def add_area(df: pd.DataFrame) -> None:
    df["Area"] = df["Height"]*df["Width"]


def sort_df_sy_area(df: pd.DataFrame) -> pd.DataFrame:
    return df.sort_values(by="Area")


def create_hist_by_areas(df: pd.DataFrame) -> None:
    df["Area"].plot()
    plt.title('Histogram of areas')
    plt.xlabel('Image')
    plt.ylabel('Area')
    plt.show()
