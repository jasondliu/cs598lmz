from lzma import LZMADecompressor
LZMADecompressor.decompress(data)

# pyflate
import zlib
import pyflate
pyflate.decompress(data, wbits=zlib.MAX_WBITS|32)

# gzip
import zlib
import flask
import gzip

gzip.compression()

# deflate
import deflate
import gzip
deflate.decompress(gzip.GzipFile(fileobj=io.BytesIO(row)).read()[2:-4])
