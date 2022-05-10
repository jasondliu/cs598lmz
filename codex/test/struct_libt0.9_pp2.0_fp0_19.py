import _struct
NUMBITS = 8
NUMBYTES = 3

LONG_SIZE = 8
LONG_MASK = (1 << LONG_SIZE) - 1
def encode(x, sign_extend=False):
    # TYPE: (int, bool) -> bytes
    """
    :param x: long
    :param sign_extend: return the two's complement with a leading null byte for
    compatibility with Python's struct module
    :return: bytes
    """
    return _struct.pack('>q', x) if sign_extend else _struct.pack('>Q', x)

def decode(b):
    return _struct.unpack(b'>q', b)[0]

def decode_u(b):
    return _struct.unpack(b'>Q', b)[0]
