import bz2
bz2_file = bz2.BZ2File('out.bz2')
data = bz2_file.read()

print(data)

# gzip
import gzip
gzip_file = gzip.open('out.gz', 'rt')
data = gzip_file.read()

print(data)
