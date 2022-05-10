import threading
threading.stack_size(67108864)

import os
import sys

LABEL_COUNT = 7


def create_image_lists(image_dir, testing_percentage, validation_percentage):
    """
    Builds a list of training images from the file system.

    Analyzes the sub folders in the image directory, splits them into stable training, testing, and validation sets,
    and returns a data structure describing the lists of images for each label and their paths.

    :param image_dir: String path to a folder containing subfolders of images.
    :param testing_percentage: Integer percentage of the images to reserve for tests.
    :param validation_percentage: Integer percentage of images reserved for validation.
    :return: Dictionary of label subfolder, with images split into training, testing, and validation sets within each label.
    """
    if not gfile.Exists(image_dir):
        tf.logging.error("Image directory '" + image_dir + "' not found.")
        return None
    result = {}
    sub_dirs = [x[0] for x in g
