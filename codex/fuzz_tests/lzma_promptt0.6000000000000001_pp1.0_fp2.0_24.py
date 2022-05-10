import lzma
# Test LZMADecompressor
from io import BytesIO

compressed = BytesIO()
comp = lzma.LZMACompressor(format=lzma.FORMAT_XZ,
                           check=lzma.CHECK_CRC64,
                           preset=9)
comp.compress(b'abcdefghijklmnopqrstuvwxyz')
comp.flush()

decomp = lzma.LZMADecompressor(format=lzma.FORMAT_XZ,
                               check=lzma.CHECK_CRC64)
decomp.decompress(b'abcdefghijklmnopqrstuvwxyz')

comp = lzma.LZMACompressor(format=lzma.FORMAT_ALONE,
                           check=lzma.CHECK_CRC64,
                           preset=9)
comp.compress(b'abcdefghijklmnopqrstuvwxyz')
comp.flush()

decomp = lzma.LZMADecompressor(format=l
