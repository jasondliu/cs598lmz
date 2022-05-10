import bz2
# Test BZ2Decompressor with an empty input.
decompressor = bz2.BZ2Decompressor()
try:
    decompressor.decompress(b"")
except EOFError:
    print('EOFError')
# Test BZ2Decompressor with a truncated input.
decompressor = bz2.BZ2Decompressor()
try:
    decompressor.decompress(b"BZh91AY&SY")
except EOFError:
    print('EOFError')

# Test BZ2Decompressor with a valid compressed input.
decompressor = bz2.BZ2Decompressor()
decompressor.decompress(b"BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084")
decompressor.decompress(b"BZh91AY&
