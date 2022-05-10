import lzma
# Test LZMADecompressor() class
import io
import struct

# File format:
#   +----------------+
#   | compressed_len |
#   +----------------+
#   | compressed data |
#   +----------------+
#
#   compressed_len: int, little-endian

compressed_len = struct.pack('<I', io.DEFAULT_BUFFER_SIZE)

with lzma.open('test.xz', 'rb') as f_in:
    with open('test.txt', 'wb') as f_out:
        f_out.write(compressed_len)
        while True:
            chunk = f_in.read(io.DEFAULT_BUFFER_SIZE)
            if len(chunk) == 0:
                break
            f_out.write(chunk)

with open('test.txt', 'rb') as f:
    compressed_len, = struct.unpack('<I', f.read(4))
    decompressor = lzma.LZMADecompressor()
    while True:
        chunk = f.read(io.
