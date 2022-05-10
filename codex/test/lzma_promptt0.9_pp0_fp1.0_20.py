import lzma
# Test LZMADecompressor

import io
import lzma

compressed = b'\xfd7zXZ\x00\x00\x04\xe6\xd6B\x02\x00!\x01\x16\x00\x00\x00t/\x80\x7fTHE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.\x90\x0f\xa0\x00\x00\x00\x00\x01'
fileobj = io.BytesIO(compressed)
decompressor = lzma.LZMADecompressor()
