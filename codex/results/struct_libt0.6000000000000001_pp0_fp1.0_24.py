import _struct
import StringIO

import numpy as np

from skimage import measure
from skimage import transform
from skimage import color


class RawImage():
    """
    Class to load and manipulate raw images.
    """
    def __init__(self, filename, verbose=False):
        """
        Initialize the class.

        :param filename: name of the raw file
        :param verbose: if true, print some information about the image
        """
        self.filename = filename
        self.verbose = verbose

        self.read_header()
        self.read_image()

    def read_header(self):
        """
        Read the header of the raw image.
        """
        with open(self.filename, "rb") as f:
            self.nx = _struct.unpack('i', f.read(4))[0]
            self.ny = _struct.unpack('i', f.read(4))[0]
            self.nz = _struct.unpack('i', f.read(4))[0]
            self.n
