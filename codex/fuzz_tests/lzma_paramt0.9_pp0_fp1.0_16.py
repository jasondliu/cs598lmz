from lzma import LZMADecompressor
LZMADecompressor().decompress(_test_data)
</code>
If you had data as a single bytes string, you could omit the <code>decode()</code>, but it is better to remember that data could be in either binary or text representation, so the decode makes sense. The Decompressor().feed() and Decompasser().flush() pattern is useful for streaming data (e.g., a network stream), but it is not needed here. 
The interesting part here is that the documentation of this third party library defines the feed method to turn bytes into a sequence of bytes. So you need to echo it: bytes out of bytes in. Strong typing, indeed.

