from lzma import LZMADecompressor
LZMADecompressor.__init__
...
</code>
And there is your constructor.
It should be obvious that you need to use <code>LZMADecompressor()</code> instead of <code>LZMADecompressor</code>, though. I only mention it because you seem to have some misconceptions about classes and objects. Please read some good introduction to Python classes.

