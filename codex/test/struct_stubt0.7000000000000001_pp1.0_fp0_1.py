from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('3s3sHH', 'abc', 'def')

# This function is only used in one place, but it's a good
# illustration of the kind of thing to do in C to save space.
def calcsize(fmt):
    acc = 0
    c2s_len = len(c2s)
    for c in fmt:
        acc = acc + c2s_len
    return acc

class Struct:
    def __init__(self, fmt, *args):
        self._fmt = fmt
        self._len = calcsize(fmt)
