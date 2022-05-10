import bz2
# Test BZ2Decompressor
file = bz2.BZ2File('sample.txt.bz2')
content = file.read()
decomp = bz2.BZ2Decompressor()
print(decomp.__class__.__name__)
# Decompress 1st part of file
content = file.read()
decomp = bz2.BZ2Decompressor()
content = decomp.decompress(content)
# Decompress more ...
content += decomp.decompress(file.read())
content += decomp.decompress(file.read())
file.close()
 
# Show decompressed content
print(content)
 
# Show length of decompressed content in bytes
print(len(content))

# Compare to original uncompressed file
file = open('sample.txt', 'rb')
content = file.read()
print(len(content))
print(content == content)
# Test BZ2Compressor and BZ2Decompressor
file = bz2.BZ2File('sample.txt.bz2')
content = file.read()
print(
