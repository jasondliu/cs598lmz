from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\x00\x00\x00\x00')
</code>
But it yields <code>MemoryError</code>.
<code>MemoryError                               Traceback (most recent call last)
&lt;ipython-input-2-a2c16a9b9fce&gt; in &lt;module&gt;
----&gt; 1 LZMADecompressor().decompress(b'\x00\x00\x00\x00')

/usr/lib/python3.5/lzma.py in decompress(self, data, max_length)
    726         # Read and verify the uncompressed size.
    727         if self.uncompressed_size &lt; 0:
--&gt; 728             raise NeedMoreDataError("max_length required but not given")
    729         if max_length is None:
    730             max_length = self.uncompressed_size

NeedMoreDataError: max_length required but not given
</code>
Any ideas as to how I can decompress
