import bz2
bz2_file = bz2.BZ2File(data_path('example.csv.bz2'))
print(bz2_file.readline().decode('utf-8'))
print(bz2_file.readline().decode('utf-8'))

import lzma
lzma_file = lzma.open(data_path('example.csv.xz'))
print(lzma_file.readline().decode('utf-8'))
print(lzma_file.readline().decode('utf-8'))


# Writing compressed data
with gzip.open(data_path('out.csv.gz'), 'wt') as f:
    f.write(text)

with bz2.open(data_path('out.csv.bz2'), 'wt') as f:
    f.write(text)

with lzma.open(data_path('out.csv.xz'), 'wt') as f:
    f.write(text)

# Reading and writing compressed data with pandas
import
