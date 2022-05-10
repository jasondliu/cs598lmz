import bz2
# Test BZ2Decompressor manually

f = open("../data/bz2/enwik8.bz2", "rb")
d = bz2.BZ2Decompressor()

for i in range(10):
    next_chunk = d.decompress(f.read(1024))
    print()
    print("Chunk {}:".format(i))
    print("Length of raw data: {}".format(len(next_chunk)))
    print("Raw data:")
    print(next_chunk)

f.close()
 
# Use BZ2File to decompress a BZ2 file

f = bz2.BZ2File("../data/bz2/enwik8.bz2")
for i in range(10):
    next_chunk = f.read(1024)
    print()
    print("Chunk {}:".format(i))
    print("Length of raw data: {}".format(len(next_chunk)))
    print("Raw data:")
    print(next_chunk)
    print("Decoded data:")
