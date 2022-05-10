import bz2
# Test BZ2Decompressor
bz2_decompressor = bz2.BZ2Decompressor()
test_data = open("test_data.txt.bz2","rb").read()
print(bz2_decompressor.decompress(test_data))

# Test BZ2Compressor
bz2_compressor = bz2.BZ2Compressor()
print(bz2_compressor.compress(b"Hello World!"))
print(bz2_compressor.flush())

# Test open
bz2_file = bz2.open("test_data.txt.bz2","rt")
print(bz2_file.read())
print("Close bz2 file")
bz2_file.close()

# Test BZ2File
bz2_file = bz2.BZ2File("test_data.txt.bz2","rt")
print(bz2_file.read())
print("Close BZ2File")
bz2_file.close()
