import lzma
lzma.LZMADecompressor().decompress(open('./test.lzma', 'rb').read())
</code>
I've tried looking through the documentation, but I can't find any mention of this.
I'm running Python 3.2.2 on Ubuntu 10.04, and lzma is version 4.999.9beta from the Ubuntu repositories.  I'm not sure if this is a Python or lzma issue.


A:

I did some more digging, and it turns out that the problem is that the file is corrupted.  It's not a bug in Python or the lzma library.

