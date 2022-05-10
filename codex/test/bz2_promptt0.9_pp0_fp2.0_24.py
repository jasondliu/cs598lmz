import bz2
# Test BZ2Decompressor.read(n) with a large value of n.
# If the compressed data provided to the decompressor is too large,
# read() will return an error object (e.g. OverflowError).
# Python 2.7 truncates the argument to read() to 2147483904,
# and this test fails, but it passes on Python 3.
decompressor = bz2.BZ2Decompressor()
try:
    decompressor.decompress(b'\x00' * 100, sys.maxsize)
except:
    pass
# Test BZ2Compressor.compress(data) after decompressing invalid data.
# The Python 2.7 BZ2Compressor object has been initialized with the empty
# string, but the Python 3.4 BZ2Compressor object has not been initialized.
# Both Python 2.7 and 3.4 raise errors when the data is compressed.
try:
    decompressor.decompress(b'\x00')
except:
    good_compressor = bz2.BZ2Compressor()
