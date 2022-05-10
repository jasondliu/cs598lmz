import bz2
# Test BZ2Decompressor.readinto(...) issues
decomp = bz2.BZ2Decompressor()
dat = decomp.unconsumed_tail
l = 1
while l > 0:
    dat += decomp.decompress(dat)
    bs = bytearray(1024)
    l = decomp.decompress_readinto(bs)
    print(bs[:l].decode('latin1'), end='')
try:
    issubclass(int, float)
except Exception as err:
    print(err.__class__)
    print(err)

print(issubclass(float, int))
from datetime import tzinfo, timedelta
from math import log

class FixedOffsetTZ(tzinfo):
    def __init__(self, hours, name):
        self.__hours = timedelta(hours=hours)
        self.__name = name

    def __repr__(self):
        return "<FixedOffset %r>" % (self.__name,)

    def __str__(self):
        return self.__name

    def utco
