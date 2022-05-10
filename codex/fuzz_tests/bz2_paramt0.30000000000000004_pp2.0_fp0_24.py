from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

# bz2_data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
# print(bz2_data)
# print(BZ2Decompressor().decompress(bz2_data))

# import zlib
# zlib_data = zlib.compress(b'witch which has which witches wrist watch')
# print(zlib_data)
# print(zlib.decompress(zlib_data))

# import gzip
# with gzip.open('somefile.gz', 'rb') as f:
#     f_content = f.read()
#     print(f_content)

# import gzip
# with gzip.open('somefile.gz', 'wt') as f:
