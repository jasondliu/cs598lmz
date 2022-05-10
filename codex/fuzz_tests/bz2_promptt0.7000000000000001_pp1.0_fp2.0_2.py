import bz2
# Test BZ2Decompressor
data = b"BZh91AY&SY.\xc5N\x18\x00\x01>_\x80\x00\x10@\x02\xff\xf0\x01\x07n\x00?"
bz2_decompressor = bz2.BZ2Decompressor()

try:
    result = bz2_decompressor.decompress(data)
except EOFError:
    result = bz2_decompressor.unused_data

print(result)

print(bz2_decompressor.eof)

bz2_decompressor.decompress(b'\x00\x00\x00\x00')

print(bz2_decompressor.eof)
# decompress()
import bz2
# data = bz2.compress(b"this is a test")
data = b"BZh91AY&SY.\xc5N\x18\x00\x01>_\x80\x00\x10@\x02\
