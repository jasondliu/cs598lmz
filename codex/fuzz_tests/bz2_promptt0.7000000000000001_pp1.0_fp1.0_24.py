import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
decompressor.decompress(compressed_data)

# Test BZ2Compressor
compressor = bz2.BZ2Compressor()
compressor.compress(data)
compressor.flush()
print(len(compressed_data))
print(compressor.compress(data))

# 使用compress()和decompress()函数更简单
print(bz2.decompress(compressed_data))
print(bz2.compress(data))

# 使用bz2.open()函数使用BZ2File

with bz2.open('test.bz2', 'w') as output:
    output.write(data)
with bz2.open('test.bz2', 'r') as input:
    print(input.read())
"""
"""
# 打包压缩
import tarfile
import zipfile

#
