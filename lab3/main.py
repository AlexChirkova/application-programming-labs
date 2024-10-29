import argparse
import cv2 as cv


from workimage import show_hist_rgb, create_hist_rgb, reflection


def get_input_info() -> tuple:
    """
    Parsing the arguments of command line
    :return: tuple of name od directory, request, name of annotation file
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('path_to_img', type=str, help='name dir')
    parser.add_argument('path_to_save', type=str, help='request')
    parser.add_argument('reflection_axis', type=str, help='annotation_file')
    args = parser.parse_args()
    path_to_img, path_to_save, reflection_axis = args.path_to_img, args.path_to_save, args.reflection_axis
    return path_to_img, path_to_save, reflection_axis


def main() -> None:
    path_to_img, path_to_save, reflection_axis = get_input_info()

    try:
        img = cv.imread(path_to_img)
        print(f"{path_to_img} sizes: {img.shape}")
        show_hist_rgb(create_hist_rgb(img))

        ref_img = reflection(img, int(reflection_axis))
        cv.imshow("Original image", img)
        cv.waitKey(0)
        cv.imshow("Reflected image", ref_img)
        cv.waitKey(0)

        cv.imwrite(path_to_save, ref_img)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
