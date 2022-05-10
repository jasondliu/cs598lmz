import codecs
codecs.register_error('ignore', codecs.lookup("UTF8"))

from multiprocessing import Pool
from functools import partial
from PIL import Image
from shapely.geometry import Polygon
from os import path, makedirs
from random import randint


from tqdm import tqdm
from tqdm import trange
from itertools import chain

from deepfool import deepfool
from deepfool import deepfool_batch
from deepfool import utils
from deepfool import deepfool_resnet_cifar10


NUM_OF_CLASSES = 10
TRANSPARENT = (0, 0, 0, 0)
MAX_DISTANCE_TO_ROI = 2.8
MAX_IMAGE_SIZE = 128
MIN_IMAGE_SIZE = 32
MAX_BATCH_SIZE = 1000
MIN_BLACKLIST_CAPACITY = 1000
MAX_BLACKLIST_CAPACITY = 100000
BLACKLIST_EXPIRE_PERIOD = 500


def normalize_image(data):
    return (data.astype(
