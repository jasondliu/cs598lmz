from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

print(bz2_data.decode('utf-8'))

"""
# pickle

import pickle

data = {
    'a': [1, 2.0, 3, 4+6j],
    'b': ("character string", b"byte string"),
    'c': {None, True, False}
}

data_string = pickle.dumps(data)
data_from_string = pickle.loads(data_string)
print(data_from_string)

data_from_string == data

# lzma

import lzma

with lzma.open('file.xz', 'wt') as f:
    f.write(text)

with lzma.open('file.xz', 'rt') as f:
    text_from_file = f.read()

print(text_from_file)

# gzip

import gzip

with gzip.open('file.gz', 'wt') as f:
    f.write
