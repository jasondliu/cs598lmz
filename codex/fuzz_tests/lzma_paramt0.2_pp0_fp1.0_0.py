from lzma import LZMADecompressor
LZMADecompressor.decompress(b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\x00\x00\x00\x00')

# decompress
import lzma
with lzma.open('file.xz', 'rt') as f:
    file_content = f.read()

# compress
import lzma
with lzma.open('file.xz', 'wt') as f:
    f.write(file_content)

# compress
import lzma
with lzma.open('file.xz', 'wt', preset=9 | lzma.PRESET_EXTREME) as f:
    f.write(file_content)

# compress
import lzma
with lzma.open('file.xz', 'wt', preset=9 | lzma.PRESET_EXTREME) as f:
    f.write(file_content)

#
