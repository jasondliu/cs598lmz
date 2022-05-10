import lzma
lzma.LZMAFile = lzma.LZMAFile
from .._hvexceptions import *

from . import ATechWriter

class XMA(object):
    """
    Reader for XMA files used in Infinity Engine games.
    """
    #from struct import unpack as struct_unpack

    def __init__(self, filename=None):
        self.reset(filename)

    def reset(self, filename=None):
        if filename:
            self.open(filename)
            self.read()

    def open(self, filename):
        """
        Open `filename` and save it as a file-like object.
        """
        with open(filename, 'rb') as self.f:
            self.f.seek(0)
            # Make sure we're reading a XMA file
            try:
                header = self.f.read(4)
                header_magic, header_version = struct_unpack("<4sI", header)
            except:
                raise InvalidXMAFile("{0} is not a valid XMA file.".format
