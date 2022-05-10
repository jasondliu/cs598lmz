import bz2
# Test BZ2Decompressor
with bz2.open(os.path.join(path, 'sample.bz2'), 'rb') as f:
    decompressor = bz2.BZ2Decompressor()
    content = decompressor.decompress(f.read())
    print(content.decode())

# Test BZ2File
with bz2.BZ2File(os.path.join(path, 'sample.bz2'), 'rb') as f:
    content = f.read()
    print(content.decode())

# Test writing
with bz2.BZ2File(os.path.join(path, 'sample.bz2.copy'), 'wb') as f:
    f.write(content)

# Test compressing
with bz2.BZ2File(os.path.join(path, 'sample.bz2.copy'), 'wb') as f:
    f.write(b'Lots of data here')

# Test compressing
with open(os.path.join(path, 'sample.bz2.copy'), 'rb')
