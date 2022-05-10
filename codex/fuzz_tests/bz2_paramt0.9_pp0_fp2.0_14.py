from bz2 import BZ2Decompressor
BZ2Decompressor()
</code>
and 
<code>from lzma import LZMADecompressor
LZMADecompressor()
</code>
which I then used to decompress the file into a string
<code># This code is incomplete, and only included for illustration purposes
with open("input.txt.bz2", "rb") as inputfile:
    decompressor = BZ2Decompressor()
    content = decompressor.decompress(inputfile.read())
</code>

