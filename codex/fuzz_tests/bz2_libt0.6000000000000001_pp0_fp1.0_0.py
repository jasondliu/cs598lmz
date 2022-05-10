import bz2
bz2_compressor = bz2.BZ2Compressor()

with open('example.csv.bz2', 'wb') as f:
    for line in open('example.csv', 'rt'):
        f.write(bz2_compressor.compress(line.encode('utf-8')))
    f.write(bz2_compressor.flush())
bz2_compressor = bz2.BZ2Compressor()
with open('example.csv.bz2', 'wb') as f:
    for line in open('example.csv', 'rt'):
        f.write(bz2_compressor.compress(line.encode('utf-8')))
    f.write(bz2_compressor.flush())
import bz2
bz2_compressor = bz2.BZ2Compressor()
with open('example.csv.bz2', 'wb') as f:
    for line in open('example.csv', 'rt'):
        f.write(bz2_compressor.compress(line.
