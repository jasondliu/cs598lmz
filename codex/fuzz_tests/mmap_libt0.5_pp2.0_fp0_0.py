import mmap
import os

from . import config
from . import log
from . import utils

class File(object):
    """
    A file object that can be used to read/write to a file on disk.
    """

    def __init__(self, path, mode='r', **kwargs):
        """
        Initialize a file object.

        :param str path: the path to the file
        :param str mode: the mode to open the file in
        :param kwargs: any keyword arguments to pass to the open function
        """

        self.path = path
        self.mode = mode
        self.kwargs = kwargs

        self.file = None

    def __enter__(self):
        """
        Open the file for reading/writing.

        :returns: self
        """

        self.file = open(self.path, self.mode, **self.kwargs)
        return self

    def __exit__(self, *args):
        """
        Close the file.
        """

        self.file.close()

    def __iter__
