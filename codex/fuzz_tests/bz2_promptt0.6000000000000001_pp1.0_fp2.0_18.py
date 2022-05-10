import bz2
# Test BZ2Decompressor
bz_file = bz2.BZ2File("test.txt.bz2")
bz_file.read()

# Test BZ2Decompressor
bz_decomp = bz2.BZ2Decompressor()
bz_decomp.decompress(bz_file.read())

# Test BZ2File
bz2_file = bz2.BZ2File("test.txt.bz2")
bz2_file.read()

# Test BZ2File.readlines
bz2.BZ2File("test.txt.bz2").readlines()

# Test BZ2File.seek
bz2.BZ2File("test.txt.bz2").seek(0)

# Test BZ2File.tell
bz2.BZ2File("test.txt.bz2").tell()

# Test BZ2File.write
bz2.BZ2File("test.txt.bz2").write(bz2.BZ2File("test.txt.b
