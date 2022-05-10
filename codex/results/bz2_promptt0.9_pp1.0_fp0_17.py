import bz2
# Test BZ2Decompressor.softspace behaviour
decompressor = bz2.BZ2Decompressor()
decompressor.softspace = 42
# Test BZ2Decompressor.unused_data behaviour
def feeder(data, block_size):
    yield data[:block_size]
    yield data[block_size:] + 'a' * 10000
with open('test.bz2', 'rb') as f:
    data = f.read()
unused_data = decompressor.decompress(data, size=14)
"".join(decompressor.unused_data)
 
expected = sys.stdin.read()
len(expected)
with open('test.bz2', 'rb') as f:
    bz2file = bz2.BZ2File(f)
bz2file.seek(0)
bz2file.read(20)
bz2file.seek(-5, os.SEEK_CUR)
bz2file.read(14)
bz2file.seek(-5, os.SEEK_CUR)
b
