from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# from lzma import LZMADecompressor
# c = LZMADecompressor()
# c.decompress(b'\x01')
# c.decompress(b'y\x00\x04\x00\x00\xc0\x02\x00\x00\x00')
# c.decompress(b'\x8b\x04\x00\x00\x00\x00\x00\x00\x00')

# import tempfile
# import lzma
# import xattr
# with tempfile.TemporaryDirectory() as temp_dir:
#     filename = os.path.join(temp_dir, 'lzma_file')
#     with lzma.open(filename, mode='wt') as f:
#         f.write('some data')
#
#     data = b'example attribute'
#     xattr.setxattr(filename, 'user.comment', data)
#
#     xdata = xattr.getxattr(filename
