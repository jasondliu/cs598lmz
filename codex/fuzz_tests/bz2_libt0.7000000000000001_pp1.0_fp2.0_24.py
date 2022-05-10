import bz2
bz2.decompress(data)

#如果是文件对象，也可以这么写
bz2_file = bz2.BZ2File('bz2_file.bz2')
bz2_file.read()
