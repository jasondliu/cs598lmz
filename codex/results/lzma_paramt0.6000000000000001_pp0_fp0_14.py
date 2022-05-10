from lzma import LZMADecompressor
LZMADecompressor.decompress(open(filename, 'rb').read()).decode('utf-8')

# from lzma import open
# f = LZMAFile(filename)
# text = f.read()

# import lzma
# import sys
# xzcat = lzma.LZMADecompressor()
# with open(filename, 'rb') as f:
#     for line in f:
#         sys.stdout.buffer.write(xzcat.decompress(line))
#         sys.stdout.buffer.flush()

# import gzip
# import bz2
# import zipfile
# import tarfile
# import lzma

# import sys
# import gzip
# import bz2
# import lzma
# import zipfile
# import tarfile

# with gzip.open(filename, 'rt') as f:
#     text = f.read()

# with bz2.open(filename, 'rt') as f:
#     text = f.read()

# with lzma.open
