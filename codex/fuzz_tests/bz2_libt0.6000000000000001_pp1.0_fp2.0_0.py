import bz2
bz2.compress(''.join(str(i) for i in range(1,11))) #returns a compressed string

bz2.decompress(bz2.compress(''.join(str(i) for i in range(1,11))))

#reading and writing in binary mode
f = bz2.BZ2File('file.bz2', 'w')
f.write(''.join(str(i) for i in range(1,11)))
f.close()

f = bz2.BZ2File('file.bz2', 'r')
print(f.read())
f.close()
