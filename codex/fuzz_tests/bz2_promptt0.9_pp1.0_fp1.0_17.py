import bz2
# Test BZ2Decompressor()
compressed_data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
decompressor = bz2.BZ2Decompressor()
data = decompressor.decompress(compressed_data)
data

# test CompressFile()
out = io.BytesIO()
output = bz2.BZ2File(out, 'w', compresslevel=9)
output.write(b'abcdefghijklmnopqrstuvwxyz')
output.close()
out.seek(0)
out.read()

####
import zlib
s = b'witch which has which witches wrist watch'
len(s)

t = zlib.compress(s)
len(t)
zlib.decompress(t)

zlib.c
