import bz2
# Test BZ2Decompressor class
f = bz2.BZ2File('example.bz2')
f.read()

f = bz2.BZ2File('example.txt.bz2', 'wb')
f.write(b'hello world')
f.close()

f = bz2.BZ2File('example.bz2')
f.read()

import bz2
# Test BZ2File class
bz_file = bz2.BZ2File('example.bz2')
for line in bz_file:
    print(line)

bz_file = bz2.BZ2File('example.bz2')
line = bz_file.readline()
bz_file.seek(0)

f = bz2.BZ2File('example.txt.bz2', 'w')
f.write(b'Hello')
f.write(b'World')
f.close()

# Compress the data
data = bz2.compress(b'hello world')
bz2.decomp
