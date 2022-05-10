import _struct
from _struct import unpack, calcsize

class StructU(object):

    def __init__(self, fmt):
        self._fmt = fmt

    def __call__(self, data):
        return unpack(self._fmt, data)


class StructC(object):

    def __init__(self, fmt):
        self._fmt = fmt

    def __call__(self, *args):
        return pack(self._fmt, *args)


def generate(fmt):
    size = calcsize(fmt)

    if isinstance(size, int):
        u = StructU(fmt)
        c = StructC(fmt)
        return (size, u, c)

    return generate
