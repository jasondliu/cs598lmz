import bz2
bz2.decompress(bytes(encode_image))

# bz2.decompress(encode_image)

import bz2
un = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
pw = b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
print(bz2.decompress(un))
print(bz2.decompress(pw))

import xmlrpc.client
proxy = xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php
