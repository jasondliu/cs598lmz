from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

# 由于解压缩后的数据可能会包含多个文件，因此返回的数据是一个包含每个文件内容的列表。
# 如果只有一个文件，那么返回的只是一个字符串。

# 如果你想压缩数据并将它们写入到一个文件对象中去，可以使用 BZ2File() 函数。
# 比如：

with open('somefile.bz2', 'wb') as f:
    f.write(data)

with BZ2File('some
