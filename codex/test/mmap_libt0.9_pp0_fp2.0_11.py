import mmap
import logging
import os.path

LOG = logging.getLogger(__name__)


def in_bounds(image_size, bounds):
    [height, width] = image_size[:2]
    [x, y, w, h] = bounds
    if x < 0 or x > width:
        return False
    if y < 0 or y > height:
        return False
    return True


def get_description(description_file):
    with open(description_file) as f:
        description_data = json.load(f)
    return description_data


def get_image_size(filename):
    image = cv2.imread(filename)
    return image.shape


def find_next_photo(taken_photos, initialized_photos):
    '''finds the next image that still needs to be processed'''
    for i, taken_photo in enumerate(taken_photos):
        if not os.path.exists('{}.jpg'.format(taken_photo[0])):
            continue
