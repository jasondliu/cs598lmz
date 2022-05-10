from lzma import LZMADecompressor
LZMADecompressor().decompress(msg)
</code>


A:

<code>&lt;class 'bytes'&gt;
</code>
'b' is just a flag. The class is bytes. You can convert bytes to bytearray or unicode by decoding. 
<code>bytes_ = b'blah blah'
bytearray_ = bytes_.decode('utf-8')
</code>

