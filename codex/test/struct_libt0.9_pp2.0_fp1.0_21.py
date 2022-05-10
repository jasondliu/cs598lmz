import _struct
from ctypes import sizeof, addressof, cast, pointer, POINTER, c_bool, c_char, c_char_p, c_int, c_double, c_float, c_void_p, c_wchar, c_wchar_p
from ctypes import Structure, Union, Array

from collections import namedtuple
import re

from audiostream import *
from audeo import *

from . import _audeo
from .functions import *


class FILE(Structure):
    pass


c_FILE_p = POINTER(FILE)

def fdopen(fd, mode="r", bufsize = -1):
    _audeo.ffi.Cdef("""
#define _O_BINARY 0

static __inline__ FILE *fdopen(int fd, const char *mode)
{
    return _fdopen(fd, mode);
}""")

