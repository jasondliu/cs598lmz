import bz2
bz2.decompress(b).decode('utf-8')

# bz2.BZ2File()
# bz2.BZ2File.write()
# bz2.BZ2File.read()
# bz2.BZ2File.close()

# bz2.compress()
# bz2.decompress()

with bz2.BZ2File('sample.bz2', 'w') as fp:
    fp.write(b'bz2 compress sample data!')

with bz2.BZ2File('sample.bz2', 'r') as fp:
    print(fp.read())
