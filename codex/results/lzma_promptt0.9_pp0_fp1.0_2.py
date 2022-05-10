import lzma
# Test LZMADecompressor
src = lzma.LZMADecompressor
print("SRC version:", src.__version__)
print("SRC name:", src.__name__)

import lzma_wrapper
# Test my wrapper
w = lzma_wrapper.LZMADecompressor
print("WRAPPER version:", w.__version__)
print("WRAPPER name:", w.__name__)
</code>
Output:
<code>SRC version: None
SRC name: compress
WRAPPER version: None
WRAPPER name: compress
</code>
What is the right way to do it?


A:

<code>LZMADecompressor.compress</code> is already a bound method and doesn't need to be rebound in the way you are doing it.
First, define <code>LZMADecompressor.__init__()</code> as:
<code>def __init__(self, format=FORMAT_AUTO, check=-1, preset=None, filters=None):
    lzma.LZ
