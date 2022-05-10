from bz2 import BZ2Decompressor
BZ2Decompressor.decompress = new_decompress
del new_decompress
del BZ2Decompressor
</code>
The discussions here and here suggest that the problem may be due to a bug in the module on Python 2.6. So in the meantime, you may want to update the Python version on your server.

