import bz2
# Test BZ2Decompressor
output = ObfuscatedCliqueSampling(BZ2Decompressor(open(defaultpath_compressed_graph,'rb')),1000,S,N)
i=0
for v in output:
    print(v)
    i+=1
    if i==3:
        break

sum(output)

# Test GZipDecompressor
output = ObfuscatedCliqueSampling(GZipDecompressor(open(defaultpath_compressed_graph,'rb')),1000,S,N)
i=0
for v in output:
    print(v)
    i+=1
    if i==3:
        break

sum(output)
 
# Test LZMADecompressor
output = ObfuscatedCliqueSampling(LZMADecompressor(open(defaultpath_compressed_graph_xz,'rb')),1000,S,N)
i=0
for v in output:
    print(v)
    i+=1
    if i==3:
        break

sum(output)
 
# Test LZMADec
