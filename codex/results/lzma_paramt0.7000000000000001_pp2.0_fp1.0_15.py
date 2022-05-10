from lzma import LZMADecompressor
LZMADecompressor(format=FORMAT_ALONE).decompress(compressed_data)

# 只支持纯数据
# uncompressed_data = lzma.decompress(compressed_data)
# print(uncompressed_data)

# 压缩到文件
# with lzma.open("filename.xz", "w") as f:
#     f.write(b"Hello, world!")

# 解压缩
# with lzma.open("filename.xz") as f:
#     file_content = f.read()

# 7z 压缩
# import subprocess
# subprocess.run(["7z", "a", "-t7z", "my_archive.7z", "mydir"])

# 压缩文件
# import gzip
# with open('somefile.gz', 'wt') as f:
#     f.write(data)

# 压缩文件
