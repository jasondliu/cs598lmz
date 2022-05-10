import bz2
bz2.decompress(bz2_data)

# 压缩
bz2_data = bz2.compress(data)

# 压缩文件
bz2.compress(open('/path/to/file', 'rb').read())

# 压缩文件
bz2.BZ2File('/path/to/file.bz2', 'wb').write(data)

# 解压文件
bz2.BZ2File('/path/to/file.bz2', 'rb').read()

# 压缩文件
with bz2.BZ2File('/path/to/file.bz2', 'wb') as f:
    f.write(data)

# 解压文件
with bz2.BZ2File('/path/to/file.bz2', 'rb') as f:
    file_content = f.read()
