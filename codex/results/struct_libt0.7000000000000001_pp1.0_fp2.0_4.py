import _struct

_INT_SIZE = 4
_NULL_TERM_SIZE = 1

def _read_int(f):
    return _struct.unpack("i", f.read(_INT_SIZE))[0]

def _read_string(f):
    if _read_int(f) != 0:
        raise IOError("Non-null-terminated string")
    return f.read(_read_int(f))

def _write_int(f, i):
    f.write(_struct.pack("i", i))

def _write_string(f, s):
    _write_int(f, 0)
    _write_int(f, len(s))
    f.write(s)

class Node(object):
    def __init__(self, key, left, right):
        self.key = key
        self.left = left
        self.right = right

def _read_node(f):
    key = _read_int(f)
    left_exists = _read_int(f)
    right_exists =
