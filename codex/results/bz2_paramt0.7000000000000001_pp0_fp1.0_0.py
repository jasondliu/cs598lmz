from bz2 import BZ2Decompressor
BZ2Decompressor.decompress(compressed_text)

decompressed_text = BZ2Decompressor().decompress(compressed_text)
print(decompressed_text)

import gzip
with gzip.open('example.txt.gz', 'rt') as input_file:
    print(input_file.read())

import gzip
with gzip.open('example.txt.gz', 'wt') as output_file:
    output_file.write('Contents of the example file go here.\n')

import gzip
with gzip.open('example.txt.gz', 'wt') as output_file:
    output_file.write('Contents of the example file go here.\n')

with gzip.open('example.txt.gz', 'rt') as input_file:
    print(input_file.read())

import zipfile
with zipfile.ZipFile('example.zip', 'w') as output_zip:
    output_zip.write('example.txt')

import zipfile
with zipfile.ZipFile('example.zip', '
