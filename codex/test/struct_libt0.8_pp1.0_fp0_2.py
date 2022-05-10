import _struct
from . import util

def _pad(s, n):
    pad = b'\x00'
    if len(s) + n < 0:
        raise struct.error('padding overflow')
    return s + (n - len(s)) * pad

def _pack_int(num, size):
    if num < 0:
        raise struct.error('cannot pack negative value')
    return _pad(util.to_bytes(num), size)

def _pack_str(s, n=None):
    if not n:
        n = len(s)
    if len(s) > n:
        raise struct.error('string too long')
    return _pad(s, n)

def _unpack_int(data, size):
    return util.from_bytes(data[:size])

def _unpack_str(data, n=None, b=True):
    n = n or len(data)
    return data[:n]

