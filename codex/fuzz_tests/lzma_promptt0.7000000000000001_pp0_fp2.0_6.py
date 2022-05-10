import lzma
# Test LZMADecompressor
d = lzma.LZMADecompressor()
out = d.decompress(c)
print(out)

print("\n")
print("lzma.open(file, mode='r', format=None, check=-1, preset=None, filters=None)")
print("======================================================================")
print("Create an LZMA-file object, which can be used to read or write LZMA-compressed data.\n")
print("It supports the file protocol in Python 3.7 and above.\n")
print("The file argument can be either a path-like object or an open file descriptor (an integer). If it is a path, the file will be opened and closed by lzma.open(). If it is an open file descriptor, no file opening or closing operations are performed by lzma.open().\n")
print("The mode argument can be 'r' (the default) for reading, 'w' for (over)writing, or 'x' for exclusive creation.\n")
print("The format argument can be None (the default), 'xz' or 'lzma'.
