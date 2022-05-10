import bz2
# Test BZ2Decompressor
zd = bz2.BZ2Decompressor()
data = zd.decompress('BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')
zd.decompress(data[-1:])

# Test open
bz2.open('/dev/null', mode='w')
bz2.open('/dev/null', mode='w', compresslevel=9)
bz2.open('/dev/null', mode='w', encoding='utf-8')
bz2.open('/dev/null', mode='w', compresslevel=9, encoding='utf-8')
bz2.open('/dev/null', mode='w', encoding='utf-8', errors='ignore')
bz2.open('/dev/null', mode='w', compresslevel=9,
