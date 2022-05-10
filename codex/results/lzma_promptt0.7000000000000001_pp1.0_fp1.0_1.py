import lzma
# Test LZMADecompressor
#
#   >>> decompress = LZMADecompressor()
#   >>> decompress.decompress(b'XZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00')
#   b'witch which has which witches wrist watch'
#   >>> decompress.decompress(b'\x00\x00\x00\x00')
#   b'witch which has which witches wrist watch'
#   >>> decompress.flush()
#   b'\n'
#   >>> decompress.decompress(b'XZ\x00\x00\x04\xe6\xd6\xb4F\x00\x00\x00\x00\x02\x00\x00\x00')
#   Traceback (most recent call last):
#     ...
#   OSError: Invalid input data
#   >>> decompress.decompress(b'XZ\x00\x00\x04\xe6')
