from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)
</code>
The code is a little bit long.
I want to decompress the data in the fastest way.
I tried to use the code below:
<code>import bz2
bz2.decompress(data)
</code>
It is also slow.
How can I do it?
Thank you.


A:

You can use the <code>decompress()</code> method of the <code>BZ2Decompressor</code> object:
<code>import bz2

data = b'BZh91AY&amp;SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07&lt;]\xc9\x14\xe1BA\x06\xbe\x084'

comp = bz2.BZ2Decompressor()

comp.decompress(data)

# 'BZh91AY&amp;SY\x
