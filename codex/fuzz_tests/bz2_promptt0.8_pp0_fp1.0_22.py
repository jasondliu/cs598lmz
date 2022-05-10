import bz2
# Test BZ2Decompressor.flush with a predefined compressed file.
bz2_file = bz2.BZ2File(TESTFN_BZ2)
bz2_compressor = bz2.BZ2Compressor()
data = bz2_file.read()
bz2_file.close()
uncompressed_data = b''
while True:
    chunk = bz2_compressor.compress(data)
    if chunk:
        uncompressed_data += chunk
    else:
        break
uncompressed_data += bz2_compressor.flush()
with open(TESTFN, 'wb') as f:
    f.write(uncompressed_data)
with bz2.BZ2File(TESTFN, 'r') as f:
    bz2_data = f.read()
os.remove(TESTFN)
# The file TESTFN contains the original test file.
with bz2.BZ2File(TESTFN_BZ2, 'r') as f:
    test_data = f.read()
# The data read
