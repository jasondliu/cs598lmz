import bz2
# Test BZ2Decompressor which is not a stream
data = bz2.decompress(bz2_data)
data
 
bzip2_f = bz2.BZ2File('data/decompressed.txt.bz2')
bzip2_f.read()

with open('data/file_to_compress.txt') as f:
    start_size = f.tell()
    f.seek(0, 2)
    end_size = f.tell()
start_size

print(end_size)
 
# Compress the file with BZ2 compression
with bz2.BZ2File('data/file_to_compress.txt.bz2', 'w') as f:
    f.write(bz2_data)
# Decompress the file with BZ2 compression
with bz2.BZ2File('data/file_to_compress.txt.bz2', 'r') as f:
    data = f.read()
data

with open('data/file_to_compress.txt', 'rb') as f
