from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2.BZ2File('enwiki-latest-pages-articles.xml.bz2').read())
</code>
This gives me the decompressed data. But I can't seem to write it to a file. I tried <code>open('enwiki-latest-pages-articles.xml','w').write(decompressed_data)</code> but it gives me an error.


A:

You're trying to write a <code>bytes</code> object to a file opened in text mode.  You need to open the file in binary mode:
<code>open('enwiki-latest-pages-articles.xml','wb').write(decompressed_data)
</code>

