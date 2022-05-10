import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with open('data/enwik8.bz2', 'rb') as f:
    data = f.read(100000)
    text = decompressor.decompress(data)
    text = text.decode('utf8')
    
print(text[:500])
# We can use the BZ2File class

with bz2.BZ2File('data/enwik8.bz2') as f:
    data = f.read(100000)
    text = data.decode('utf8')
    
print(text[:500])
# Or the decompress() function

with open('data/enwik8.bz2', 'rb') as f:
    data = f.read(100000)
    text = bz2.decompress(data)
    text = text.decode('utf8')
    
print(text[:500])
# Test BZ2Compressor

compressor = bz2.BZ2Compressor()
text = '
