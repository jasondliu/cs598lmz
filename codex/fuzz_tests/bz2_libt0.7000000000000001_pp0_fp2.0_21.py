import bz2
bz2.BZ2Compressor().compress(b"hello")

# compression.py

# bzip2 is block-sorted by default and gives better compression rates
# than gzip, but is slower
import bz2

original_data = b'This is the original text.'
print('Original     :', len(original_data), original_data)
compressed = bz2.compress(original_data)
print('Compressed   :', len(compressed), compressed)
decompressed = bz2.decompress(compressed)
print('Decompressed :', len(decompressed), decompressed)


# gzip will use the .gz extension when compressing

import gzip

with gzip.open('somefile.gz', 'wt') as f:
    f.write('Contents of the file')

with gzip.open('somefile.gz', 'rt') as f:
    file_content = f.read()

# gzip is a simple file format that compresses individual files.
# It is not designed to hold multiple files.

# zip
