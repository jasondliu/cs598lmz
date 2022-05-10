from bz2 import BZ2Decompressor
BZ2Decompressor()
</code>
Which surprisingly worked, hence the question. According to the docs the <code>decompress</code> method is not supposed to work.
Would like to know why this works and this is the correct answer. (Or if it's a bug, in which case I'm not sure how to constrain this).
Updates on this bug:

https://bugs.python.org/issue23362
https://bugs.python.org/issue34104



A:

I think this is an error in the documentation. The <code>bz2</code> module only supports one-shot decompression. However <code>BZ2Decompressor.decompress</code> works like a stream decompressor, that is it can be called multiple times. The <code>bz2</code> module does not support streams, but <code>BZ2Decompressor</code> does.
<code>BZ2Decompressor()</code> creates a decompressor object that works like a stream. <code>BZ2Decompressor().decompress(data)</code> works like the one-shot decompression, i
