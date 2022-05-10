import lzma
# Test LZMADecompressor
import io
rawio = io.BytesIO(b'\xfd7zXZ\x00\x00\x04\xe6\xd6B\x02\x00!\x01\x16\x00\x00\x00t/\x00\x00\x00\x00')
dcomp = lzma.LZMADecompressor()
dcomp.decompress(rawio.read())

# Test LZMADecompressor.decompress with multiple calls to read
import io
rawio = io.BytesIO(b'\xfd7zXZ\x00\x00\x04\xe6\xd6B\x02\x00!\x01\x16\x00\x00\x00t/\x00\x00\x00\x00')
dcomp = lzma.LZMADecompressor()
dcomp.decompress(rawio.read())
dcomp.decompress(b'')

# Test LZMADecompressor.decompress with multiple calls to
