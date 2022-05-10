from lzma import LZMADecompressor
LZMADecompressor.flush = lambda self, _: ""
</code>
then you can use <code>bz2</code> and <code>lzma</code> modules just like you would normally. But if you want to go further, I would try using <code>importlib</code>. Essentially you'd write your own modules that wrap the functionality you need from <code>io</code>, <code>bz2</code>, and <code>lzma</code>, then use <code>importlib</code> to load the module you need at run-time.

