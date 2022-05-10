from lzma import LZMADecompressor
LZMADecompressor.decompress(data)
</code>
I also tried writing the data to a file using <code>with open('path', 'wb') as f: f.write(data)</code> and running the following command in the terminal:
<code>xzcat path</code>
But both give me this error:
<blockquote>
<p>b''</p>
<p>Traceback (most recent call last):</p>
<p>File "", line 1, in </p>
<p>ValueError: Input format not a lzma stream</p>
</blockquote>
How should I go about decompressing this?

