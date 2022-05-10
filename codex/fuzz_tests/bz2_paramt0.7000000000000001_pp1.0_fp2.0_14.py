from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(compressed)
</code>
Output:
<code>'BZh91AY&amp;SY\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07&lt;]\xc9\x14\xe1BA\x06\xbe\x084'
</code>
which is exactly the same as in your question.

