import bz2
# Test BZ2Decompressor

decomp = bz2.decompressobj()
b = open(datapath+'bz2_compressed.bin', 'rb').read()  # bytes object
bz = decomp.decompress(b)
bz  

p = open(datapath+'bz2_compressed.bin', 'rb')
print('Test BZ2Decompressor')
for n,line in enumerate(bz2.BZ2Decompressor(p).readlines(),1):
    print(line.rstrip().decode())
p.close()
# Test BZ2File
# The bz2.BZ2File class works like a regular text file, supporting
# standard read, readline, readlines, write, writelines, and close
# methods.

print('Test BZ2File, write')
p = bz2.BZ2File(datapath+'bz2_log.bz2', 'w')
# Output to the compressed file is automatically chunked and compressed
for line in open(datapath+'cookbook/somefile
