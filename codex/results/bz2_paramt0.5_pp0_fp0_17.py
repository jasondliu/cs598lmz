from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2.decompress(data))

# bz2.decompress(data)

# def my_bz2_decompress(data):
#     if data[0:3] == b'BZh':
#         return BZ2Decompressor().decompress(data)
#     else:
#         return data

# my_bz2_decompress(data)

# import gzip
# gzip.decompress(data)

# def my_gzip_decompress(data):
#     if data[0:2] == b'\x1f\x8b':
#         return gzip.decompress(data)
#     else:
#         return data

# my_gzip_decompress(data)

# import lzma
# lzma.decompress(data)

# def my_lzma_decompress(data):
#     if data[0:6] == b'\xfd7zXZ\x00':
#        
