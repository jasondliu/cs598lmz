import bz2
bz2_file = bz2.BZ2File('data/text.bz2')
bz2_file.read()

# Compress with bz2
import bz2
with open('data/text.txt', 'rb') as original:
    data = original.read()
with bz2.BZ2File('data/text.bz2', 'wb') as compressed:
    compressed.write(data)

# Decompress with bz2
import bz2
with bz2.BZ2File('data/text.bz2', 'rb') as compressed:
    data = compressed.read()
with open('data/text.txt', 'wb') as original:
    original.write(data)

# Compress with gzip
import gzip
with open('data/text.txt', 'rb') as original:
    data = original.read()
with gzip.GzipFile('data/text.gz', 'wb') as compressed:
    compressed.write(data)

# Decompress with gzip
import gzip
with gzip.
