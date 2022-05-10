from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(compressed_data)

# 简单压缩文件
with open('something.bz2', 'wb') as output_file, open('something.txt', 'rb') as input_file:
    with contextlib.closing(BZ2Compressor(9)) as comp:
        output_file.write(comp.compress(input_file.read()))
        output_file.write(comp.flush())

# lzma 压缩和解压缩
import lzma

with open('file.xz', 'rb') as f:
    file_content = f.read()

uncompressed = lzma.decompress(file_content)

with lzma.open('file.xz', 'rb') as f:
    file_content = f.read()

with lzma.open('file.xz', 'wt', encoding='utf-8') as f:
    f.write(text)


# 压缩数
