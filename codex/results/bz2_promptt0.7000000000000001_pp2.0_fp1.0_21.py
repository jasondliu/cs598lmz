import bz2
# Test BZ2Decompressor class

decomp = bz2.BZ2Decompressor()

try:
    while True:
        data = decomp.decompress(src.read(10))
        if not data:
            break
        dst.write(data)
except IOError:
    pass
 
dst.close()
src.close()
 
# Test BZ2Compressor class
src = open("test.txt", "rb")
dst = open("test1.txt.bz2", "wb")

comp = bz2.BZ2Compressor()

while True:
    data = src.read(10)
    if not data:
        break
    dst.write(comp.compress(data))

dst.write(comp.flush())

dst.close()
src.close()
 
# Test open method
src = open("test.txt", "rb")
dst = bz2.open("test1.txt.bz2", "wb")

dst.writelines(src)

dst.close()
src.
