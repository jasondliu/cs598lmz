import mmap
import os
import re
import sys
import time
import threading
import traceback
import weakref
import zipfile

from . import compat, archive, util

__all__ = ['File', 'FileSystem', 'FileSystemError', 'UnicodeMixin']

def _check_path_encoding(path):
    """
    Ensure that the given path is encoded using the file system encoding.
    """
    try:
        if not isinstance(path, str):
            path = path.decode(sys.getfilesystemencoding())
    except UnicodeDecodeError:
        raise UnicodeEncodeError('path contains non-ASCII characters')
    return path

class UnicodeMixin:
    """
    A base class for implementing a class that requires unicode support.

    This class is a mixin, and must be inherited from to be used.
    """
    @property
    def name(self):
        """
        The unicode name of the class.
        """
        return self._name

    @property
    def path(self):
        """
        The unicode
