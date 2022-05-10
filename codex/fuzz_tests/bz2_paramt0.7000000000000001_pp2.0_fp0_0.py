from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(gzip.open('scored_genes.txt.bz2').read())
</code>
And the error I get is:
<code>  File "/usr/lib/python2.7/bz2.py", line 174, in decompress
    return self._buffer.read()
AttributeError: 'str' object has no attribute 'read'
</code>
I don't know how to fix it, and I can't find the reason of the error. I am a newbie in this, I am learning. I have a file with thousands of genes and I just want to find some of them and then extract the information about their score. 
Any help would be appreciated!
Thanks!


A:

<code>gzip.open</code> returns a file-like object, not a string.
Use:
<code>file = gzip.open('scored_genes.txt.bz2')
bzdata = file.read()
BZ2Decompressor().decompress(bzdata)
</code>
or
<code>BZ2Decompressor().
