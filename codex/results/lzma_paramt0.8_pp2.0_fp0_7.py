from lzma import LZMADecompressor
LZMADecompressor().decompress(lzma_data)
</code>
At the time of writing, these ports are not yet available in a stable release (3.5.0 or 3.5.1).  They are in the subversion repository, however, so you can get <code>pylzma</code> using
<code>easy_install -i http://www.lfd.uci.edu/~gohlke/pythonlibs/ lzma
</code>
Note that <code>pylzma</code> is not a pure Python implementation.  It is a Python wrapper around liblzma, which is the same C library used by 7-zip.  If you trust 7-zip, you should be able to trust the liblzma implementation of the LZMA algorithm.

