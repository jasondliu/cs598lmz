import mmap
import re
import sys
import time

from functools import partial
from multiprocessing import Pool
from typing import Optional, Tuple, List, Callable

import cv2
import numpy as np

from . import config
from . import models
from . import plot


def read_image(file_path: str) -> Tuple[np.array, str]:
    """Read an image, normalizing the pixel values to be in [0, 1]"""
    img = cv2.imread(file_path)
    img = img / 255.0

    return img, file_path


def read_images(file_paths: List[str]) -> List[Tuple[np.array, str]]:
    """Read a batch of images in parallel, normalizing the pixel values to be in [0, 1]"""
    with Pool(config.NUM_PROCESSES) as pool:
        images = pool.map(read_image, file_paths)

    return images


def get_file_paths(data_dir: str, filter: Optional[str
