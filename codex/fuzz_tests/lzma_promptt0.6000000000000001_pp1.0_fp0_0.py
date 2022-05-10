import lzma
# Test LZMADecompressor.decompress(), LZMADecompressor.eof(), and LZMADecompressor.flush()

# Test invalid arguments
for args in [(), (0,), (0, 0)]:
    try:
        lzma.LZMADecompressor().decompress(*args)
    except TypeError:
        pass
    else:
        print("TypeError not raised when calling LZMADecompressor.decompress with %s" % (args,))

# Test various valid calls
decompressor = lzma.LZMADecompressor()
try:
    decompressor.decompress(b"")
except EOFError:
    pass
else:
    print("EOFError not raised when calling LZMADecompressor.decompress() with no data")

try:
    decompressor.decompress(b"x")
except EOFError:
    pass
else:
    print("EOFError not raised when calling LZMADecompressor.decompress() with incomplete data")

try:
   
