import bz2
bz2.decompress("BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084")

#we get 'huge'

bz2.decompress("BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08")

#we get 'file'

'huge'+'file'

#we get 'hugefile'



import urllib.request
import re
mypage = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=12345').read()


#we need to
