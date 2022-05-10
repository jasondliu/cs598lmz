import mmap
import os
import re
import sys

from . import _compat
from . import _util
from . import _version
from . import _xattr
from . import _xattrs

if sys.platform == 'win32':
    import win32file
    import win32con
    import pywintypes
    import winerror

__all__ = [
    'XAttrMetadata',
    'XAttrSet',
    'XAttrMap',
    'XAttrFile',
    'XAttrKeyError',
    'XAttrOSError',
    'XAttrNotImplementedError',
    'XAttrUnsupportedError',
    'XAttrIOError',
    'XAttrNotFoundError',
    'XAttrPermissionError',
    'XAttrInvalidNameError',
    'XAttrInvalidValueError',
    'XAttrValueTooLongError',
    'XAttrNoSpaceError',
    'XAttrNotAFileError',
    'XAttrNotADirectoryError',
    '
