from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# 可以使用incrementaldecompress()方法一部分一部分的解压数据
decompressor = LZMADecompressor()
while True:
    chunk = file.read(1024)
    if not chunk:
        break
    data = decompressor.decompress(chunk)
    if data:
        sys.stdout.write(data)
    else:
        sys.stderr.write('Error in decompression\n')
        sys.exit(1)

# 使用LZMAFile类，可以像普通文件那样操作压缩文件
with lzma.open('example.xz', 'rt') as f:
    print(f.read())

# 可以使用open()函数打开一个压缩文件
