import mmap
import sys
from struct import unpack_from, calcsize

from msl.loadlib import Server32, Server64
from msl.loadlib.common import open_shared_library
from msl.loadlib.mapper import Mapper32, Mapper64

try:
    FileNotFoundError
except NameError:
    FileNotFoundError = IOError


class LoadLibrary(object):

    def __init__(self, filename, mode='r', handle=None):
        """
        Load a shared library into memory.

        Parameters
        ----------
        filename : :class:`str`
            The name of the shared library to load.
        mode : :class:`str`
            The mode to open the shared library in.
        handle : :class:`int`, optional
            If specified, then an already open shared library is specified and the `filename`
            is ignored.
        """
        self._filename = filename
        self._mode = mode
        self._handle = handle
        self._functions = {}

        # create the memory mapper and load the DLL
       
