from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# https://stackoverflow.com/questions/1838699/how-can-i-decompress-a-gzip-stream-with-zlib
import zlib
zlib.decompress(data, 16+zlib.MAX_WBITS)
