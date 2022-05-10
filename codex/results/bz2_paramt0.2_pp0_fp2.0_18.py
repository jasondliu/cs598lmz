from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(open('enwiki-latest-pages-articles.xml.bz2', 'rb').read())

# or

import bz2
bz2.decompress(open('enwiki-latest-pages-articles.xml.bz2', 'rb').read())
</code>

