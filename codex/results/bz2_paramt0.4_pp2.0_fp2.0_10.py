from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)
</code>
but the output is a bunch of gibberish.
I'm not sure what I'm doing wrong here.  Any help would be appreciated.


A:

The file is compressed in the <code>bz2</code> format, so you need to use the <code>bz2</code> module to decompress it.
<code>import bz2

with open('file.bz2', 'rb') as f:
    data = f.read()

print(bz2.decompress(data))
</code>

