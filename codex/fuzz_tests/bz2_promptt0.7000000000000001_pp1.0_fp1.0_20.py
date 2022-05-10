import bz2
# Test BZ2Decompressor
d = bz2.BZ2Decompressor()
with open(r'C:\Users\Jiang Tao\Downloads\test.bz2') as f:
    decompressed_data = d.decompress(f)
decompressed_data

# 使用 BZ2File
with bz2.BZ2File(r'C:\Users\Jiang Tao\Downloads\test.bz2', 'rb') as f:
    decompressed_data = f.read(100)
decompressed_data

decompressed_data = b''
with bz2.BZ2File(r'C:\Users\Jiang Tao\Downloads\test.bz2', 'rb') as f:
    for data in iter(lambda : f.read(100), b''):
        decompressed_data += data
decompressed_data

# 压缩
compressed_data = bz2.compress(b"This is a test")
compressed_data

len(b"This is a test")
len(compressed_data
