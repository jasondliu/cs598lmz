import bz2
bz2_data = 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
print ''.join(bz2.BZ2Decompressor().decompress(bz2_data.decode('base64')).splitlines())

# LEVEL 7
import Image
inImg = Image.open('oxygen.png')
im = inImg.getdata()
imLen = inImg.size[0]
row = [im[x][0] for x in xrange(0, imLen, 7)]
rowStr = ''.join([chr(x) for x in row])
result = [105, 110, 116, 101, 103, 114, 105, 116, 121]
print ''.join([chr(x) for x in result])

# LEVEL 8
import bz2
un
