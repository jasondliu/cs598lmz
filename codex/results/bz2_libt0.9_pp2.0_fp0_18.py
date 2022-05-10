import bz2
bz2.decompress(b'BZh91AY&SY.86\xc8N\x18\x00\x00\x00\x00\x80\x00\x10@\x00\x00\x00\x02\xff\xf4\x00\x01\x00a\x00d')

b'\x00\x00\x00\x00\x80\x00\x00\x00\x04\x00\x00\x00\x06\x00\x00\x00\x00'
</code>
The uncompressed data is just the raw byte data.
Now take it another step and use a regex to remove out the hex code, and you have the string version of the data.
<code>import bz2
from re import compile, match
bz2.decompress(b'BZh91AY&amp;SY.86\xc8N\x18\x00\x00\x00\x00\x80\x00\x10@\x00\x00\x00\x02\
