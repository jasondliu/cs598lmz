import bz2
bz2.compress(b'1234567890')

with bz2.BZ2File('example.bz2', 'wb') as output:
    with open('example', 'rb') as input:
        for line in input:
            output.write(line)

'''
bz2.compress(string)
bz2.decompress(compressed_string)

bz2.BZ2Compressor()
bz2.BZ2Decompressor()

bz2.BZ2File(filename, mode, **kwargs)
bz2.BZ2File和open函数类似，但它的文件模式只能是只读模式r或者只写模式w，并且还需要指定一个后缀名为bz2的文件名。

'''

from bz2 import BZ
