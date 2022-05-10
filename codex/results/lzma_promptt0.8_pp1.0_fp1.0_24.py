import lzma
# Test LZMADecompressor

cd = lzma.LZMADecompressor()
data = cd.decompress(inp)
print(len(data))
# Test LZMACompressor

cm = lzma.LZMACompressor()
comp = cm.compress(data)
print(len(comp))
# Test LZMADecompressor

cd = lzma.LZMADecompressor()
data2 = cd.decompress(comp)
print(len(data2))
data == data2
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

