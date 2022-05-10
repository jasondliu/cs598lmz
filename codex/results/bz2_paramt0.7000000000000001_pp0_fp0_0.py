from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(o)

#bz2.BZ2File(o).read()

a = bz2.decompress(o)
print(a)
#print(bz2.decompress(o))

#print(o)
#print(bz2.decompress(o))

#with bz2.open(o, 'r') as f:
#    data = f.read()
#print(data)
