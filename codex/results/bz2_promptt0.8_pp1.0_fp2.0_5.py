import bz2
# Test BZ2Decompressor's read()
dec = bz2.BZ2Decompressor()
try:
    dec.decompress(open('bz2test.txt.bz2', 'rb').read())
finally:
    del dec

# Test BZ2File
print(open('bz2test.txt.bz2', 'rb').read())
print(bz2.open('bz2test.txt.bz2', 'r', 0, 200, 100).read())
print(bz2.open('bz2test.txt.bz2').read())
print(open('bz2test.txt.bz2', 'rb', 0, 200, 100).read())

# Test BZ2Compressor's compress()
print(bz2.compress('hello'))

# Test BZ2Compressor's flush()
comp = bz2.BZ2Compressor()
try:
    comp.compress('hello')
    comp.flush()
finally:
    del comp

# Test BZ2File's write()
bz2.open
