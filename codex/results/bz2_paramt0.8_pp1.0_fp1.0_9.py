from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(b'BZh91AY&SY\xc4\x98\x00\x00\x00\x01\x00\x00\x00\x80\x00\x10@\x00 \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'))

with open('../data/log.txt.bz2') as log_file:
    decompressor = BZ2Decompressor()
    for line in log_file:
        decoded_line = decompressor.decompress(line)
        print(decoded_line)

#LZMA
#
#The lzma module includes a class for the LZMA compression format, and is fully compati-
#ble with the LZMA SDK. The lzma module is a wrapper for the XZ utilities and provides
#access to the individual compression algorithms. The lzma module also supports some
#of the LZMA2 features, but the compression format is not fully compatible with the LZMA
#SDK
