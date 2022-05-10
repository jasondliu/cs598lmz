import bz2
# Test BZ2Decompressor.readinto()

infile = bz2.BZ2File(test_support.TESTFN, mode="wb")
infile.write("xxx")
infile.close()

infile = bz2.BZ2File(test_support.TESTFN, mode="rb")
outfile = open(test_support.TESTFN + "-out", mode="wb")
cd = bz2.BZ2Decompressor()
cd.decompress("XXX")
cd.decompress("XXX")
cd.decompress("XXX")
cd.decompress("XXX")
while True:
    buf = cd.unused_data
    if buf:
        outfile.write(buf)
        cd.unused_data = ""
    data = infile.read(1024)
    if data == "":
        break
    cd.decompress(data)
outfile.close()
infile.close()

testout = open(test_support.TESTFN+"-out", mode="rb").read()
assert testout == "xyzzy"*
