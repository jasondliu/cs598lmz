from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')

with urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/integrity.html') as res:
    the_page = res.read()
    print(the_page)
