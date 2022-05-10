import lzma
lzma.LZMAFile()

from utils import iterate_over_files, last_path_component

def get_image(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    # Numpy load by row, so resize the image to have the correct orientation
    image = cv2.resize(image, (64, 64))
    return image

def get_images(image_paths):
    image_array = [get_image(image_path) for image_path in image_paths]
    return image_array

def get_data(image_paths):
    images = get_images(image_paths)
    images = np.array(images, dtype=np.float32)
    images = np.reshape(images, [-1, 64, 64, 1])
    return images


def encode_data(image_paths, compression_level=6):
    images = get_data(image_paths)
    data = np.packbits(images)
