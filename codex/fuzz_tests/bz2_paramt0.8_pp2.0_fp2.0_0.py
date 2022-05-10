from bz2 import BZ2Decompressor
BZ2Decompressor.decompress = _patched_decompress

from zlib import decompress as _patched_decompress
from zlib import Decompress as _Decompress
_Decompress.decompress = _patched_decompress

if __name__ == '__main__':
    from collections import namedtuple
    from itertools import product

    class Flag(object):
        @classmethod
        def __new__(cls, value):
            if not isinstance(value, str):
                value = chr(value)
            return value

    class Flags(object):
        def __init__(self, flags):
            self.flags = flags
        def __iter__(self):
            for flag in self.flags:
                yield Flag(flag)
        def __reversed__(self):
            for flag in reversed(self.flags):
                yield Flag(flag)

    class A(object):
        def __init__(self, index):
            self.index = index
        def __repr__(self):
            return 'A%03d
