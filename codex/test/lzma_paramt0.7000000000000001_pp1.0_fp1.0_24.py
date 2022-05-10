from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\x00\x00\x80\x00\x00\x00\x07\x00\x02\x00')

b'\x00\x00\x80\x00\x00\x00\x07\x00\x02\x00'.hex()

#import binascii
#binascii.unhexlify('00 00 80 00 00 00 07 00 02 00'.replace(' ', ''))

#b'\x00\x00\x80\x00\x00\x00\x07\x00\x02\x00'.decode('utf-8')
