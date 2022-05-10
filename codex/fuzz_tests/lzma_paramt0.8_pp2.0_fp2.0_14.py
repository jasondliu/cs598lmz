from lzma import LZMADecompressor
LZMADecompressor(format=FORMAT_RAW, filters=None)
</code>
First, it returns <code>Exception: LZMA library error</code>
So, it seems to expect some other data for the <code>filters</code> parameter. I suppose it will be the <code>filters</code> that are actually used. But what is the problem here?

