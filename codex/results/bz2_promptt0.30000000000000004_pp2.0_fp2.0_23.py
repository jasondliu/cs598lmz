import bz2
# Test BZ2Decompressor.decompress()

# Test decompression of a short string
decompressor = bz2.BZ2Decompressor()
assert decompressor.decompress(b"BZh91AY&SY") == b"hello"

# Test decompression of a long string
decompressor = bz2.BZ2Decompressor()
assert decompressor.decompress(b"BZh91AY&SY\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084") == b"hello"

# Test decompression of a short string with multiple calls to decompress()
decompressor = bz2.BZ2Decompressor()
assert decompressor.decompress(b"BZh91AY&SY") == b"hello"
assert decompressor.decompress(b"") == b""

# Test decompression of a long
