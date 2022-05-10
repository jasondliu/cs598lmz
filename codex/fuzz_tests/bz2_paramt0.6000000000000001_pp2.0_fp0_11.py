from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(open('enwiki-latest-pages-articles.xml.bz2', 'rb').read())
</code>
The last line gives the following error:
<code>OSError: Invalid data stream</code>
I am running Python 3.5.0 on Windows 8.1.

