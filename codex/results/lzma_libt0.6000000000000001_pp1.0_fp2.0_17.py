import lzma
lzma.decompress(data)

# https://stackoverflow.com/questions/1838699/how-can-i-decompress-a-gzip-stream-with-zlib
import zlib
zlib.decompress(data, 15+32)

# https://stackoverflow.com/questions/1089662/python-inflate-and-deflate-implementations
import zlib
zlib.decompress(data)
