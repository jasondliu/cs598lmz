import ctypes
import ctypes.util
import threading
import sqlite3

from io import BytesIO
import sys
from typing import Union, Iterable, Optional, Tuple
from PIL import Image
import numpy as np

from .base import BaseImage
from . import data_dir, _get_logger

if sys.platform == 'win32':
    import win32api
    import win32con


_log = _get_logger()

QT_KDE = 'QT_QPA_PLATFORMTHEME=KDE'

IMAGE_PATH = os.path.join(data_dir, 'image.png')
WINDOW_PATH = os.path.join(data_dir, 'window.png')
TASK_PATH = os.path.join(data_dir, 'task.png')
TASK_BUTTON_PATH = os.path.join(data_dir, 'task_button.png')


class ImageBuffer(object):
    def __init__(self, image: BaseImage):
        self.image = image.grab()
        self.buf = BytesIO()

    def __enter
