import bz2
bz2_file = bz2.BZ2File('test.bz2', 'r')
data = bz2_file.read()
bz2_file.close()

print(len(data))
print(data[:10])

import gzip
gzip_file = gzip.GzipFile('test.gz', 'r')
data = gzip_file.read()
gzip_file.close()

print(len(data))
print(data[:10])
