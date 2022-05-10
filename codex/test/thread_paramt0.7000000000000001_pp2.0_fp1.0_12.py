import sys, threading
threading.Thread(target=lambda: sys.stdout.write("\x1b[2J\x1b[H")).start()

import numpy as np
import os
import sys
import time
from copy import copy

from ImageManager import ImageManager, Location
from Interval import Interval
from Footprint import Footprint

from PIL import Image

class Board(object):

    def __init__(self, size, name = None, directory = None):
        """
        A board consists of a size, a name, and a directory.
        """
        self._size = size
        self._name = name
        self._directory = directory

        self._images = {}
        self._footprints = {}

        # TODO: fix this
        self._turn = 1

    def __str__(self):
        return "Board(size = {0}, name = {1}, directory = {2}, images = {3})".format(
            self._size, self._name, self._directory, self._images)

