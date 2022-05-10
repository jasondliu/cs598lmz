from lzma import LZMADecompressor
LZMADecompressor().decompress(bytes)

#返回值是解压之后的字节流

#要解压Gzip压缩的字节流,可以使用gzip.decompress()

#如果想直接读取zip文件,可以使用zipfile.ZipFile

with zipfile.ZipFile('/tmp/example.zip') as zf:
    print(zf.namelist())
    info = zf.getinfo('README.txt')
    print(info.file_size)
    print(info.compress_size)
    print('Compressed file is %sx smaller!' %(round(info.file_size/info.compress_size, 2)))

#读取zip文件

#如果想把内存中的数据压缩后写入
