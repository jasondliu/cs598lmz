import bz2
# Test BZ2Decompressor class

decompressor = bz2.BZ2Decompressor()

# Create a file object to read from
with open('sample.bz2', 'rb') as f:
    data_in = f.read()

# Create a file object to write to
with open('sample.txt', 'wb') as f:
    f.write(decompressor.decompress(data_in))

# Test BZ2Decompressor.decompress() function

with bz2.BZ2File('sample.bz2', 'rb') as fr, \
     open('sample.txt', 'wb') as fw:
    fw.write(fr.read())

# Test BZ2File.read() function

with bz2.BZ2File('sample.bz2', 'rb') as fr, \
     open('sample.txt', 'wb') as fw:
    for chunk in iter(lambda: fr.read(1024), b''):
        fw.write(decompressor.decompress(chunk))

# Test b
