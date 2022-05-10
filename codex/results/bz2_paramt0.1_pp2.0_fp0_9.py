from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2.compress(b'hello world!'))

# bz2.BZ2Compressor
# bz2.BZ2Decompressor

# bz2.compress(data, compresslevel=9)
# bz2.decompress(data)

# bz2.open(filename, mode='r', compresslevel=9, encoding=None, errors=None, newline=None)

# bz2.BZ2File(filename, mode='r', buffering=None, compresslevel=9, encoding=None, errors=None, newline=None)

# bz2.BZ2File.close()
# bz2.BZ2File.closed
# bz2.BZ2File.detach()
# bz2.BZ2File.fileno()
# bz2.BZ2File.flush()
# bz2.BZ2File.isatty()
# bz2.BZ2File.mode
# bz2.BZ2File.name
# bz2
