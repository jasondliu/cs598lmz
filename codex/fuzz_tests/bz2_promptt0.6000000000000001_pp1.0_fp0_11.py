import bz2
# Test BZ2Decompressor
data = b'BZh91AY&SY.\xc9N\x18\x00\x00\x00\x80\x00\x10@\x80\x00\x00%\x04\x00!\x04\xe0\x04.\x00\x00\x00'

decompressor = bz2.BZ2Decompressor()

decompressor.decompress(data)

# decompressor.flush()

# Test BZ2File
with bz2.BZ2File('file.bz2') as f:
    for line in f:
        print(line)

with bz2.open('file.bz2') as f:
    for line in f:
        print(line)

with bz2.open('file.bz2', mode='wt') as f:
    f.write('The same line written twice.\n')
    f.write('The same line written twice.\n')

with bz2.open('file.bz2', mode='wt')
