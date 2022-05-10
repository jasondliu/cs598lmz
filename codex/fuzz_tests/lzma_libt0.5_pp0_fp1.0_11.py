import lzma
lzma.open

# with lzma.open('/Users/simon/Downloads/test.xz', 'rt') as f:
#     print(f.read())

import gzip
gzip.open

# with gzip.open('/Users/simon/Downloads/test.gz', 'rt') as f:
#     print(f.read())

import bz2
bz2.open

# with bz2.open('/Users/simon/Downloads/test.bz2', 'rt') as f:
#     print(f.read())

# import tarfile
# with tarfile.open('/Users/simon/Downloads/test.tar.gz', 'r:gz') as t:
#     print(t.getnames())
#     for member_info in t.getmembers():
#         print(member_info.name)
#         f = t.extractfile(member_info)
#         if f is not None:
#             print(f.read())

import zipfile
with zipfile.
