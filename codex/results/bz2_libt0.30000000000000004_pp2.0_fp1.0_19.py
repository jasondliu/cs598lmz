import bz2
bz2.decompress(bz2_data)

# bz2.BZ2File()
with bz2.BZ2File('sample.bz2') as f:
    print(f.read())

# bz2.compress()
with open('sample.txt', 'rb') as f:
    data = f.read()

with bz2.BZ2File('sample.bz2', 'wb') as f:
    f.write(data)

# bz2.decompress()
with bz2.BZ2File('sample.bz2', 'rb') as f:
    data = f.read()

with open('sample.txt', 'wb') as f:
    f.write(data)
