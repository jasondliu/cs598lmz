from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2.compress(b'Hello World!'))

# bz2.BZ2File
# 可以接受一个文件句柄，然后将其包装成一个BZ2File对象，这个对象可以被用来像处理普通文件那样处理压缩文件
with open('/tmp/example.bz2', 'rb') as input:
    with bz2.BZ2File('/tmp/example.txt.bz2', 'wb') as output:
        for data in iter(lambda: input.read(100 * 1024), b''):
            output.write(data)

# 如果你不想创建压缩文件，只是想将一个大
