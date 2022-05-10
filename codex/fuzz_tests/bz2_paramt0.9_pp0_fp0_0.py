from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data.read(4))

#写入
f = open("compressed.bz2", "wb")
f.write(BZ2Compressor().compress("写入文件"))
f.close

#打开bz2文件
f = bz2.BZ2File(filename, mode="w")
f.write("写入文件")
f.close()
f = bz2.BZ2File(filename, mode="r")
result = f.read()
test
test
test
test
test
test
test
test
test
test
test
test
test
test
test
test
test
test
test
test
test
test
test
test
test
test
test
test
test
test
test
test
test
test
test
test
test
test
test
test
test
test
test
test
test
test
test
test
test
test
test
test
test
test
test
test
test
test
test
test
