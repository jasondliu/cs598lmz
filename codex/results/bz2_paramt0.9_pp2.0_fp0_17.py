from bz2 import BZ2Decompressor
BZ2Decompressor
</code>
It works fine. The same thing using execv fails with <code>ImportError: No module named bz2</code>. I am using Ubuntu 16.04.
<code>bz2.so</code> does exist both in the active and virtual env paths. What difference does <code>execv</code> introduce?

