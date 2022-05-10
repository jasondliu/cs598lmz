import _struct
import mmap
from io import open
import fcntl
import os
from . import _ruamel_yaml as _yaml


_KERNEL_VERSION = os.uname().release
_KERNEL_MAJOR = int(_KERNEL_VERSION.split('.')[0])
_KERNEL_MINOR = int(_KERNEL_VERSION.split('.')[1])


def map_file(fd, length, offset, mode=mmap.ACCESS_WRITE):
    return mmap.mmap(fd, length, mmap.MAP_SHARED, mode, offse
