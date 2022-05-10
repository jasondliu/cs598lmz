import mmap
import os
import re
import sys
import time

import cv2
import numpy as np

from . import util
from . import constants
from . import im_util
from . import im_transform
from . import im_draw

class ImageDataset:

    def __init__(self, images_dir, labels_dir, images_ext, labels_ext,
                 images_transform=None, labels_transform=None,
                 images_loader=im_util.load_image, labels_loader=im_util.load_image,
                 images_to_tensor=im_util.image_to_tensor, labels_to_tensor=im_util.image_to_tensor,
                 images_transpose=None, labels_transpose=None,
                 images_normalize=None, labels_normalize=None,
                 images_denormalize=None, labels_denormalize=None,
                 images_to_np=None, labels_to_np=None,
                 images_to_pil=None, labels_to_pil=None,
