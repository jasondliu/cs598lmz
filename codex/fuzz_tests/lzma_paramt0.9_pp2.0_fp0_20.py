from lzma import LZMADecompressor
LZMADecompressor().decompress(file.read())
</code>
this outputs
<code>KeyError: "No "BZh" signature could be found."
</code>
this doesn't work either:
<code>import bz2
with open("wikidump.xml.bz2","rb") as file:
     bz2.decompress(file.read())
</code>
this outputs
<code>UnicodeDecodeError: 'utf8' codec can't decode byte 0xd2 in position 8:          invalid continuation byte
</code>
(and anyway the file is just 16.8M)
I don't even understand what that error message is supposed to mean.
any ideas?


A:

I can reproduce these problem on my machine using Python 3.6.7, bz2file-0.98 and lzma-3.0.2. 
Strangely, the error message is different when I replace <code>Wikimedia Commons (Commons)</code> with <code>Wikipedia (simple)</code> (everything else remains the same). 
The <code>KeyError</code> turns
