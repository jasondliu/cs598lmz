from lzma import LZMADecompressor
LZMADecompressor().decompress(file_bytes)
</code>
As a side note, the error you are getting is because <code>literal_eval()</code> only accepts string inputs, not bytes objects:
<blockquote>
<p>The string or node provided may only consist of the following Python literal structures: strings, bytes, numbers, tuples, lists, dicts, sets, booleans, and None.</p>
</blockquote>

