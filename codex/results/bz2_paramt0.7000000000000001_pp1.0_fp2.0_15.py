from bz2 import BZ2Decompressor
BZ2Decompressor()
</code>
It raises the following error:
<code>AttributeError: 'module' object has no attribute 'BZ2Decompressor'
</code>
I've tried installing bz2 via pip, easy_install, and from source from the bzip2 website, but no luck.
I'm using Python 2.7.1 on Mac OS X 10.6.4.


A:

Try:
<code>from bz2 import BZ2Decompressor
bz2decompressor = BZ2Decompressor()
</code>

