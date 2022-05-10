import bz2
# Test BZ2Decompressor object.
tar_file = bz2.BZ2Decompressor()
file = open('samples/cpg_island_ucsc.tsv.bz2', 'rb')
content = file.read()
print(tar_file.decompress(content[0:100]))
file.close()

# Test BZ2Compressor object.
comp_file = bz2.BZ2Compressor()
data = comp_file.compress(b"some text")
data += comp_file.flush()

file = open('samples/cpg_island_ucsc_comp.tsv.bz2', 'wb')
file.write(data)
file.close()
 
tar_file = bz2.BZ2Decompressor()
file = open('samples/cpg_island_ucsc_comp.tsv.bz2', 'rb')
content = file.read()
print(tar_file.decompress(content[0:100]))
file.close()

# Test BZ2File class.
cp
