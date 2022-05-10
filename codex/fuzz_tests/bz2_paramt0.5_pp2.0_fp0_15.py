from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_compressed_data)

# 压缩文件
with open('data/sample.txt', 'rb') as input:
    with bz2.BZ2File('data/sample.bz2', 'wb') as output:
        output.writelines(input)

# 解压缩文件
with bz2.BZ2File('data/sample.bz2') as input:
    print(input.read())

# 压缩和解压缩数据流
import bz2
uncompressed_data = b'The same line, over and over.\n' * 10
compressed_data = bz2.compress(uncompressed_data)
len(uncompressed_data)
len(compressed_data)

decompressor = bz2.BZ2Decompressor()
decompressed_data = decompressor.decompress(compressed_data)
decompressed_data
decomp
