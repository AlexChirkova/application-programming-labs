import cv2
import os
import pandas as pd
import matplotlib.pyplot as plt


def create_df(annotation_file: str) -> pd.DataFrame:
    """
    Creating a DataFrame
    :param annotation_file: path to annotation file
    :return: DataFrame
    """
    return pd.read_csv(annotation_file)


def add_h_w_d(df: pd.DataFrame, path_to_images: str) -> None:
    """
    Add columns: height, width, depth
    :param df: Original DataFrame
    :param path_to_images: path to dir with images
    :return: None
    """
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
    """
    Create statistic
    :param df: DataFrame to statistic
    :return: Statistical information of columns: height, width, depth
    """
    return df.loc[:, ("Height", "Width", "Depth")].agg(["min", "max", "mean"])


def filter_df_by_hw(df: pd.DataFrame, max_height: float, max_width: float) -> pd.DataFrame:
    """
    Filtering DataFrame of max height and width
    :param df: Origin DataFrame
    :param max_height: max height
    :param max_width: max width
    :return: filtered DataFrame
    """
    return df[(df["Height"] < max_height) & (df["Width"] < max_width)]


def add_area(df: pd.DataFrame) -> None:
    """
    Add column area
    :param df: Origin DataFrame
    :return: None
    """
    df["Area"] = df["Height"]*df["Width"]


def sort_df_sy_area(df: pd.DataFrame) -> pd.DataFrame:
    """
    Sorting DataFrame by areas
    :param df: Origin DataFrame
    :return: Sorted DataFrame
    """
    return df.sort_values(by="Area")


def create_hist_by_areas(df: pd.DataFrame) -> None:
    """
    Creating a hist of areas
    :param df: DataFrame
    :return: None
    """
    df["Area"].plot()
    plt.title('Histogram of areas')
    plt.xlabel('Image')
    plt.ylabel('Area')
    plt.show()
