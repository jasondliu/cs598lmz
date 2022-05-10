from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(raw)
</code>
Demo:
<code>&gt;&gt;&gt; from bz2 import BZ2Decompressor
&gt;&gt;&gt; raw = b'BZh91AY&amp;SY\x0c\xf4\x00\x00\x01\x01\x80\x03$ \x00!\x9ah3M\x13&lt;]\xc9\x14\xe1BBP\x91\xf08'
&gt;&gt;&gt; BZ2Decompressor().decompress(raw)
b"BZh91AY&amp;SY\x0c\xf4\x00\x00\x01\x01\x80\x03$ \x00!\x9ah3M\x13&lt;]\xc9\x14\xe1BBP\x91\xf08"
</code>

