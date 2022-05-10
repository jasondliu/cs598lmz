import mmap
import os
import struct

from . import flags
from . import util
from . import version
from . import vfs
from . import xattr
from .exception import FUSEError
from .filesystem import Filesystem
from .node import Node
from .pyfuse3 import FUSEError
from .statvfs import StatVFS
from .readdir import Direntry

from . import ROOT_INODE
from . import INVALID_INODE

if not hasattr(pyfuse3, 'ROOT_INODE'):
    pyfuse3.ROOT_INODE = 1


def errno_wrap(f):
    def new_func(*args, **kw):
        try:
            return f(*args, **kw)
        except FUSEError as exc:
            return exc.errno
    return new_func


class Operations(Filesystem):
    def __init__(self, *, debug=False):
        super().__init__(debug=debug)
        self.inodes = {}
