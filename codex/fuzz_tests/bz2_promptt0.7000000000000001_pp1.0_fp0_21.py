import bz2
# Test BZ2Decompressor
bz2.decompress(bz2.compress(b'hello'))

# Test BZ2Compressor
bz2.BZ2Compressor().compress(b'hello')
bz2.BZ2Compressor().flush()

# Test BZ2File
with bz2.BZ2File("test.bz2", "wb", compresslevel=9) as f:
    f.write(b'hello')
with bz2.BZ2File("test.bz2", "rb") as f:
    print(f.read())

# Test BufferedReader
with open("test.bz2", "rb") as f:
    with bz2.BZ2File("test.bz2", "rb", buffering=0) as bz2f:
        assert f.read() == bz2f.read()

# Test BufferedWriter
with open("test.bz2", "wb") as f:
    with bz2.BZ2File("test.bz2", "wb", buffering=0
