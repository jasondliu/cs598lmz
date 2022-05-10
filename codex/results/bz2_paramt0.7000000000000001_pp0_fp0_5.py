from bz2 import BZ2Decompressor
BZ2Decompressor
from base64 import b64decode
b64decode
from pickle import loads
loads
</code>
and I get no errors. So then I run 
<code>d = BZ2Decompressor()

r = d.decompress(b64decode(data, validate=True))
</code>
and I get
<code>b'\x80\x03}q\x00(X\x06\x00\x00\x00_bonusq\x01K\x05X\x04\x00\x00\x00costq\x02K\x04X\x05\x00\x00\x00dtypeq\x03X\x02\x00\x00\x00f8q\x04X\x06\x00\x00\x00fieldsq\x05X\x03\x00\x00\x00nopq\x06X\t\x00\x00\x00formdtypeq\x07X\x06\x00\x00\x00numpyq\x
