import lzma
lzma.decompress(with_segment_header)

# 在很多情况下，压缩数据可能不包含头部信息。例如，在文件系统上，压缩文件的压缩方式可以通过文件名后缀来指定。
# 要打开这样的文件，使用 open() 函数的 preset 参数指定合适的压缩级别或预设值。
with open('backup.xz', 'rb') as f:
    file_content = f.read()
    decompressor = lzma.LZMADecompressor()
    decompressed_data = decompressor.decomp
