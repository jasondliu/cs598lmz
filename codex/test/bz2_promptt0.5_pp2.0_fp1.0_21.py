import bz2
# Test BZ2Decompressor.decompress()

bz2_data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'

decompressor = bz2.BZ2Decompressor()

try:
    decompressor.decompress(bz2_data)
except EOFError:
    print('EOFError')
try:
    decompressor.decompress(bz2_data)
except EOFError:
    print('EOFError')
try:
    decompressor.decompress(bz2_data)
except EOFError:
    print('EOFError')
try:
    decompressor.decompress(bz2_data)
except EOFError:
    print('EOFError')

