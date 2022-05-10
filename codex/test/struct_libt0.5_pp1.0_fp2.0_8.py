import _struct
import _sys

def _unpack_int(data, offset, size, le):
    format = _struct.calcsize('<' if le else '>' + {1: 'B', 2: 'H', 4: 'L', 8: 'Q'}[size])
    return _struct.unpack_from('<' if le else '>' + {1: 'B', 2: 'H', 4: 'L', 8: 'Q'}[size], data, offset)[0]

def _pack_int(value, size, le):
    return _struct.pack('<' if le else '>' + {1: 'B', 2: 'H', 4: 'L', 8: 'Q'}[size], value)

def _unpack_float(data, offset, size, le):
    format = _struct.calcsize('<' if le else '>' + {4: 'f', 8: 'd'}[size])
