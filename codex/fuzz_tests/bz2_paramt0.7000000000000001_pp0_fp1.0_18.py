from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(zippedContent)
</code>
However, the output of this is just the decompressed string in binary. How can I convert this binary string to a string of unicode? I have tried:
<code>unicode(BZ2Decompressor().decompress(zippedContent)
</code>
But this does not work. 
I have also tried:
<code>BZ2Decompressor().decompress(zippedContent).decode('utf-8')
</code>
But this gives me the error:
<code>AttributeError: 'str' object has no attribute 'decode'
</code>
How can I convert a binary string to a unicode string?


A:

The word "binary" is not used in Python. <code>str</code> is a sequence of bytes. <code>unicode</code> is a sequence of characters.
<code>BZ2Decompressor().decompress(zippedContent).decode('utf-8')
</code>
This looks good, however, you need to handle the case when decoding fails.

