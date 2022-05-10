import lzma
# Test LZMADecompressor
import lzma
import io

data = b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\x00\x00\x00\x00'

with lzma.open(io.BytesIO(data)) as uncompressed:
    text = uncompressed.read()

text

# b'This is the content of the file. We are going to compress this text.'
# Test LZMAFile
import lzma
import io

data = b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\x00\x00\x00\x00'

with lzma.LZMAFile(io.BytesIO(data)) as uncompressed:
    text = uncompressed.read()

text

# b'This is
