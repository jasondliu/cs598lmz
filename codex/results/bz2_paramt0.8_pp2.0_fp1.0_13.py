from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

# a common use for compressors is to reduce the size of serialized data for
# transport.
print(len(pickle_data))
print(len(bz2_data))
print(len(lzma_data))

# in some cases, the original data can be reconstructed exactly from compressed
# data, and in other cases, only approximately.
# for example, uint8() data can be exactly reconstructed, but long integers cannot
# the floating point data from the original array may be slightly off from the
# floating point data in the recreated array.

# the compressors can also be used as context managers.
# the bz2 and lzma compressors can accept a compress level argument and if no
# value is specified, a reasonable default is used.
import bz2
with bz2.BZ2File('pickle_bzipped.pickle', 'wb') as f:
    f.write(pickle_data)

with lzma.open('pickle_lzmaed.pickle', 'wb') as f:

