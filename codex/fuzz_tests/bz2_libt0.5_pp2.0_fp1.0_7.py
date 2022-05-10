import bz2
bz2file = bz2.BZ2File('../data/wiki.bz2', 'r')

print('\n'.join(bz2file.readlines()[:10]))

bz2file.close()

with bz2.BZ2File('../data/wiki.bz2', 'r') as bz2file:
    print('\n'.join(bz2file.readlines()[:10]))

print(bz2file.closed)

bz2file = bz2.BZ2File('../data/wiki.bz2', 'r')
print(bz2file.readline())
print(bz2file.readline())
bz2file.seek(0)
print(bz2file.readline())
print(bz2file.readline())

bz2file = bz2.BZ2File('../data/wiki.bz2', 'r')
for line in bz2file:
    print(line)

bz2file = bz2.BZ
