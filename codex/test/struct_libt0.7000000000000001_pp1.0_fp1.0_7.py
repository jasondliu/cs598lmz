import _struct

from . import config
from .utils import *

#@log_exceptions
def _read_fmt(f, fmt, offset=0):
    if type(fmt) == str:
        fmt = [fmt]
    f.seek(offset)
    data = None
    for fmt in fmt:
        data = _struct.unpack_from(fmt, f.read(calcsize(fmt)))
        if len(data) == 1:
            data = data[0]
        if not data:
            continue
        break
    return data

#@log_exceptions
def _read_binary(f):
    return [int(x == b'\x01') for x in f.read()]

#@log_exceptions
def _read_index(f):
    idx = 0
