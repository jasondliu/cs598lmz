from lzma import LZMADecompressor
LZMADecompressor().decompress(open('zipped_file.xz', 'rb').read())

# 使用lzma模块压缩文件
import lzma
with lzma.open('zipped_file.xz', 'wb') as f:
    f.write(b"Hello World!")

# 解压缩文件
import lzma
with lzma.open('zipped_file.xz', 'rb') as f:
    file_content = f.read()
    print(file_content)

# 使用lzma模块压缩文件
import lzma
with lzma.open('zipped_file.xz', 'wt') as f:
    f.write("Hello World!")

# 解压缩文件
import lzma
with lzma.open('zipped_file.xz', 'rt') as f:
    file_content = f.
