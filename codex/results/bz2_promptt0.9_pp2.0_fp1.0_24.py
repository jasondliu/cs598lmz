import bz2
# Test BZ2Decompressor:


def BZ2file(filename):
    fileobj = open(filename, "rb")
    decomp = bz2.BZ2Decompressor()
    results = ""
    d = fileobj.readline()
    while d:
        results += decomp.decompress(d)
        d = fileobj.readline()
    fileobj.close()
    return results
BZ2file("text.bz2")

# Test A
import bz2
f = bz2.open("text.bz2")

res = f.read()
print(res.decode("utf-8"))

# Test B
import bz2
f = bz2.open("text.bz2")
res = f.read()
print(res)
import bz2

str = b"BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc
