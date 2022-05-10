import bz2
bz2.decompress(bz2_data)

# bz2.BZ2File
bz2_file = bz2.BZ2File('example.bz2')
bz2_file.read()
bz2_file.seek(0)
bz2_file.readlines()
bz2_file.close()

# gzip
import gzip
s = b'witch which has which witches wrist watch'
len(s)

t = gzip.compress(s)
len(t)

gzip.decompress(t)

gzip.open('example.gz', 'wt')

gzip.open('example.gz', 'wt').write('content')
gzip.open('example.gz', 'rt').read()

# zlib
import zlib
s = b'witch which has which witches wrist watch'
len(s)

t = zlib.compress(s)
len(t)

zlib.decompress(t)

zlib.crc32(s)

# l
