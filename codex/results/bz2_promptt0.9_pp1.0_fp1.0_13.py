import bz2
# Test BZ2Decompressor
d = bz2.BZ2Decompressor()
d.decompress((open(os.path.join(DATA_FOLDER, 'hp5.bz2'), 'rb').read()))[:15].decode('utf-8')

# BZ2File is the.bz2 file object

f = bz2.BZ2File(os.path.join(DATA_FOLDER, 'hp4.bz2'))
f.readline().decode('utf-8')

bz2.compress('harry potter and the goblet of fire'.encode('utf-8'))
