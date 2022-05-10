import bz2
# Test BZ2Decompressor
#
# >>> data = b'BZh91AY&SY\xc8N\x18\x00\x00\x00\x01\x01\x00\x00\xff\xff\x00\x00\xff\xff\x00\x00\x00\x00'
# >>> dec = bz2.BZ2Decompressor()
# >>> dec.decompress(data)
# b'foo'
# >>> dec.decompress(b'\x00\x00\x00\x01\x00')
# b'bar'
# >>> dec.decompress(b'\x01BZ')
# Traceback (most recent call last):
#     ...
# OSError: invalid data stream
# >>> dec.decompress(b'BZh91AY&SY\xc8N\x18\x00\x00\x00\x01\x01\x00\x00\xff\xff\x00\x00\xff\xff\x00\x00\x00\x00')
# Traceback (
