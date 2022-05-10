import lzma
lzma.decompress(compressed)

# This is not the same as compression and decompression
# in the gzip and bz2 modules, where only one of the
# two is a stream.

# The main advantage of the LZMAFile class is that
# it can be used as a context manager, just like
# other file objects.

with lzma.open('file.xz', 'wt') as f:
    f.write(text)

with lzma.open('file.xz', 'rt') as f:
    text = f.read()

# The LZMAFile class only supports the open()
# interface. It does not support the lower-level
# file interface, such as read() and write().

# The LZMAFile class also supports random access
# mode, which is not supported by the lzma module
# itself.

with lzma.open('file.xz', 'rt') as f:
    print(f.read(32))
    f.seek(0)
    print(f.read(32))


