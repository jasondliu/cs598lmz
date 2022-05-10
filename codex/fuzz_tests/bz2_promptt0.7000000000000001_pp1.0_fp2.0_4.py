import bz2
# Test BZ2Decompressor.decompress(...)
print('Test BZ2Decompressor.decompress(...)')
decompressor = BZ2Decompressor()

print('  Decompressing bytearray')
data = bytearray(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')
assert decompressor.decompress(data) == b'hello'

print('  Decompressing bytes')
data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
assert decompressor.decompress(
