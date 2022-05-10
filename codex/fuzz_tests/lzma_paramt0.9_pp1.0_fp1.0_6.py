from lzma import LZMADecompressor
LZMADecompressor().decompress(bytes.fromhex(value))

#Realiza a transfomarção necessária para aplicar o método zlib.decompress
from zlib import decompress
decompress(bytes.fromhex(value), -15)

#Realiza a transfomarção necessária para aplicar o método gzip.decompress
from gzip import decompress, compress
compress(decompress(bytes.fromhex(value), 16 + MAX_WBITS), 9)

#Realiza a transfomarção necessária para aplicar o método bz2.decompress
from bz2 import decompress, compress
compress(decompress(bytes.fromhex(value)))
