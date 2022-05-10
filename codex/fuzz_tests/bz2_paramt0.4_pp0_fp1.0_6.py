from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2.compress(b'Hello World'))

# bz2.BZ2Compressor()
# bz2.BZ2Decompressor()

# 压缩数据块
data = [b'Hello'] * 100000
with bz2.BZ2File('bz2_file.bz2', 'w') as f:
    for d in data:
        f.write(d)

with bz2.BZ2File('bz2_file.bz2', 'r') as f:
    for i, line in enumerate(f):
        if i > 10:
            break
        print(line)

# 压缩数据流
import bz2
uncompressed_data = b'Hello World. Hello World. Hello World. Hello World.'
compressor = bz2.BZ2Compressor()
compressed_data = compressor.compress(uncompressed_data)
more_data = b'Goodbye World. '
compressed
