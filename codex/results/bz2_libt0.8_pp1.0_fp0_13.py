import bz2
bz2.decompress("BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084")
#for web user agent
import re
print "".join([chr(int(x+y,16)) for x,y in re.findall("(..)(..)",bz2.decompress("BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084"))])
#for base64
import base64
base64.b64decode("YlZodTE5WXlBZlNZWA==")
#for gzip
import z
