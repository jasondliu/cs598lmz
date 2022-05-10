from lzma import LZMADecompressor
LZMADecompressor.decompress(decomp_result).decode('utf-8')
</code>
The error messages I received from the above code is:
<code>result = self.decompressobj.decompress(data, max_length)
OSError: not a valid XZ stream
</code>


A:

The <code>lzma</code> module is not compatible with <code>XZ</code>. You need to use a separate <code>pylzma</code> library.

