import lzma
lzma.decompress(lzma.compress(b'Hello'))

# 7.3.3.3 压缩和解压缩数据流
import lzma

with lzma.open('lzma_compress.xz', 'wt') as f:
    f.write('这是一个压缩的文件')

with lzma.open('lzma_compress.xz') as f:
    file_content = f.read()

print(file_content)

# 7.3.3.4 文件压缩和解压缩
import lzma

with lzma.open('lzma_compress.xz', 'wt') as f:
    f.write('这是一个压缩的文件')

with lzma.open('lzma_compress.xz') as f:
    file_content
