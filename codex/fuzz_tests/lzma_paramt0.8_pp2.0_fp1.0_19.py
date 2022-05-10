from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\x00(\x01\x00\x00\x00\x80\x06\x00\x01\xff\xff')
b''
</code>
<code>gzip</code> and <code>lzma</code> belong to the <code>_compression</code> package.
<code>sys.modules["_compression"]
&lt;module '_compression' (built-in)&gt;
</code>

