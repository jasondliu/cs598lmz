import bz2
bz2.decompress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084').decode("utf-8")

#TODO:bytearray_to_str
def bytearray_to_str(bstr):
    s = str()
    for i in range(len(bstr)):
        s = s + chr(bstr[i])
    return s

import array
array.array('B', b'\xf0\xf1\xf2\xf3\xf4').decode()

#TODO:bytes_to_str
def bytes_to_str(bs):
    return bs.decode("utf-8")

#TODO:bytes_to_text
def bytes_to_text(bs):
    return bs.dec
