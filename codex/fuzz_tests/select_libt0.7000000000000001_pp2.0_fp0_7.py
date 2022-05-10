import select_image
import argparse
import datetime

def parse_arguments():
    parser = argparse.ArgumentParser(description='Path to the folder to process')
    parser.add_argument('path', help='The path to the folder')
    args = parser.parse_args()
    return args

def main():
    start = datetime.datetime.now()
    args = parse_arguments()
    image_paths = select_image.get_image_paths(args.path)
    print("Images selected in: " + str(datetime.delta(start, datetime.datetime.now())))
    print("Calculating average for: " + str(len(image_paths)) + " images")
    start = datetime.datetime.now()
    average_image = average_images(image_paths)
    print("Average calculated in: " + str(datetime.delta(start, datetime.datetime.now())))
    cv2.imwrite("average.png", average_image)

def average_images(image_path
