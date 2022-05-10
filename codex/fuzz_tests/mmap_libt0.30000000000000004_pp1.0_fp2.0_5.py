import mmap
import os
import sys
import time

from . import errors
from . import util
from . import xattr

if sys.version_info[0] == 2:
    import cPickle as pickle
else:
    import pickle


def _get_file_size(f):
    """
    Return the size of a file.

    :param f: File object.
    :type f: file
    :returns: Size of the file.
    :rtype: int
    """
    f.seek(0, 2)
    return f.tell()


class _File(object):
    """
    A file object.

    :param filename: Filename of the file.
    :type filename: str
    :param mode: File mode.
    :type mode: str
    :param fd: File descriptor.
    :type fd: int
    :param size: Size of the file.
    :type size: int
    :param offset: Offset of the file.
    :type offset: int
    :param mmap: Memory mapped file.
   
