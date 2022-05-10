import bz2
bz2.decompress(bz2.compress(bytes(data, 'utf-8')))

# the same as above
data = 'hello world'
import zlib
zlib.decompress(zlib.compress(bytes(data, 'utf-8')))

# compress and decompress a file
import gzip
f = gzip.open('file.txt.gz', 'wb')
f.write(b'hello world')
f.close()

import gzip
f = gzip.open('file.txt.gz', 'rb')
f.read()
f.close()

# compress and decompress a file
import bz2
f = bz2.open('file.txt.bz2', 'wb')
f.write(b'hello world')
f.close()

import bz2
f = bz2.open('file.txt.bz2', 'rb')
f.read()
f.close()

# compress and decompress a file
import zlib
f = zlib.open('file.txt.zlib', '
