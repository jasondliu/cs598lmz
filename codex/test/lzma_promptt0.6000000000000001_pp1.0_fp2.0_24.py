import lzma
# Test LZMADecompressor
from io import BytesIO

compressed = BytesIO()
comp = lzma.LZMACompressor(format=lzma.FORMAT_XZ,
                           check=lzma.CHECK_CRC64,
                           preset=9)
comp.compress(b'abcdefghijklmnopqrstuvwxyz')
comp.flush()

