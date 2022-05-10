import bz2
bz2.compress(bytes([97, 98, 99, 100, 101]))

# bz2.decompress(bz2.compress(bytes([97, 98, 99, 100, 101])))

# f = bz2.BZ2File('test.bz2', 'w')
# f.write(bytes([97, 98, 99, 100, 101]))
# f.close()
#
# f = bz2.BZ2File('test.bz2', 'r')
# f.read()
