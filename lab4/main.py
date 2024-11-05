import argparse


import work_with_df as ww


def get_input_info() -> tuple:
    """
    Parsing the arguments of command line
    :return: tuple of paths to csv-file and dir with images
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('path_to_csv', type=str, help='name dir')
    parser.add_argument('path_to_images', type=str, help='name dir')
    args = parser.parse_args()
    path_to_csv, path_to_images = args.path_to_csv, args.path_to_images
    return path_to_csv, path_to_images


def main() -> None:

    try:
        path_to_csv, path_to_images = get_input_info()
        df = ww.create_df(path_to_csv)
        print(df.head())
        ww.add_h_w_d(df, path_to_images)
        print(df[["Height", "Width", "Depth"]].head())
        print("Statistic:\n", ww.statistical_information(df))
        print(ww.sort_df_by_hw(df, 1000, 1000)[["Height", "Width"]].head())
        ww.add_area(df)
        print(ww.sort_df_sy_area(df).head())
        ww.create_hist_by_areas(df)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
