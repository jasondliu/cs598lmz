import lzma
# Test LZMADecompressor.
data = lzma.compress(b'1234567890')
d = lzma.LZMADecompressor()
d.decompress(data)

print(d)

d.decompress(b'\0')
d.decompress(b'1')
d.decompress(b'234')
d.decompress(b'567890')
d.decompress(b'x')
d.flush()
print(d)

class DataAfterFlush(Exception):
    pass

# Test that the "flush" method raises ValueError if you call it after
# decompressing everything otherwise the decompress() method will
# return b"" without raising DataAfterFlush.
try:
    d.flush()
except ValueError:
    pass
else:
    raise DataAfterFlush

print("DataAfterFlush is not raised")

print("OK")
