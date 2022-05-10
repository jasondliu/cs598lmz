import bz2
bz2.decompress(bz2_compressed_data)

bz2_compressed_data = bz2.compress(data)
bz2.decompress(bz2_compressed_data)

bz2.compress(data)
bz2.decompress(bz2_compressed_data)

# chardet
import chardet
chardet.detect(b'Hello, world!')

chardet.detect(b'\xe4\xb8\xad\xe6\x96\x87')

chardet.detect(b'\xe4\xb8\xad\xff')

chardet.detect('中文'.encode('utf-8'))

chardet.detect('中文'.encode('gbk'))

# zlib
import zlib
zlib.compress(b'hello world!')

zlib.decompress(b'x\x9c+H,I-.\x00\x05\xd0\x1d\x0
