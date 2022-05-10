import bz2
# Test BZ2Decompressor
from bz2 import BZ2Decompressor
from bz2 import BZ2Compressor
from io import BytesIO

bz = BZ2Decompressor()
print(bz.decompress(compressed)) 

# Test BZ2Compressor
bz = BZ2Compressor()
bz.compress(obj)

# Test BZ2File
bz = BZ2File('test.bz2', 'r')
bz.read()

# Test BZ2File
bz = BZ2File('test.bz2', 'w')
bz.write(obj)

bz = BZ2File(BytesIO(compressed))


################################################################################
#                                Context Managers                              #
################################################################################

# contextlib.contextmanager
from contextlib import contextmanager

@contextmanager
def test_ctx(x):
    print('entering context')
    yield x

    print('exiting context')

with test_ctx() as x:
    print('inside context')

#@contextmanager
