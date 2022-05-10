from lzma import LZMADecompressor
LZMADecompressor()
</code>
I get:
<code># error: undefined symbol: PyExc_RuntimeError
</code>


A:

It seems you are missing the python development headers, or the python-dev package. Try installing that first and try again.

