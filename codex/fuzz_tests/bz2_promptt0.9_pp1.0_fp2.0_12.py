import bz2
# Test BZ2Decompressor interface

from bz2 import BZ2Decompressor
from bz2 import BZ2Compressor
from io import BytesIO

decompressor = BZ2Decompressor()
compressor = BZ2Compressor()

def test_simple():
    eq = b'helloworld' * 1000
    data = compressor.compress(eq)
    data += compressor.flush()
    obuf = BytesIO()
    obuf.write(data)
    obuf.seek(0)
    ibuf = BytesIO(data)
    ddata = decompressor.decompress(data)
    ddata += decompressor.decompress(obuf.read())
    ddata += decompressor.decompress(ibuf.read())
    ddata += decompressor.flush()
    assert eq == ddata

def test_read():
    eq = b'ab' * 500000
    data = compressor.compress(eq)
    data += compressor.flush()
    decomp = BZ2Decompressor()
    for i in range(1024):
        more
