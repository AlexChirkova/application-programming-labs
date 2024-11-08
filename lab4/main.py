import argparse


import work_with_df as ww


def get_input_info() -> str:
    """
    Parsing the arguments of command line
    :return: Name of csv-file
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('path_to_csv', type=str, help='name dir')
    args = parser.parse_args()
    path_to_csv = args.path_to_csv
    return path_to_csv


def main() -> None:

    try:
        path_to_csv = get_input_info()
        df = ww.create_df(path_to_csv)
        print(df.head())
        ww.add_h_w_d(df)
        print(df[["Height", "Width", "Depth"]].head())
        print("Statistic:\n", ww.statistical_information(df))
        print(ww.filter_df_by_hw(df, 1000, 1000)[["Height", "Width"]].head())
        ww.add_area(df)
        print(ww.sort_df_sy_area(df).head()[["Relpath", "Area"]])
        ww.create_hist_by_areas(df)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
