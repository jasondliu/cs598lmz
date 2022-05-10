import bz2
# Test BZ2Decompressor

bz_c = bz2.BZ2Compressor()
bz_d = bz2.BZ2Decompressor()

testdata = b"hello world" * 100
#testdata = b"x" * 1000000

compdata = bz_c.compress(testdata)
compdata += bz_c.flush()

print("Compressed data is %i bytes" % len(compdata))

n = 0
while True:
    decompdata = bz_d.decompress(compdata)
    n += 1
    if not decompdata or decompdata == testdata:
        break
    print("%i" % n)

if decompdata != testdata:
    print("Error")
else:
    print("Succesful.")
