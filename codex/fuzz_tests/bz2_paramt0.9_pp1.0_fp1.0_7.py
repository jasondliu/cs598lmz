from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(compressed_data)  # raise
</code>
<blockquote>
<p>OSError: Not a compressed or uncompressed <code>&lt;code&gt;bzip2&lt;/code&gt;</code> stream</p>
</blockquote>
Compression in python follows the same rules, for example:
<code>&gt;&gt;&gt; b = BZ2Compressor()
&gt;&gt;&gt; b.compress(b'foo')
b''
&gt;&gt;&gt; b.compress(b'foo')
b''
&gt;&gt;&gt; b.flush()
b'BZh91AY&amp;SY\xd6O\x00\x06B\x001\x0c\x00&amp;\x00@(\x01\x03\x0c\x05'
</code>
In short, compression creates one or more packets. If you try to decompress() the middle of a packet, the decompressor will most likely raise an error.

