from lzma import LZMADecompressor
LZMADecompressor().decompress(data)
</code>
If you want to decompress the data in a file, you can use the <code>LZMAFile</code> class:
<code>from lzma import LZMAFile
LZMAFile(filename).read()
</code>
If you want to compress data, you can use the <code>LZMACompressor</code> class:
<code>from lzma import LZMACompressor
LZMACompressor().compress(data)
</code>
If you want to compress data to a file, you can use the <code>LZMAFile</code> class:
<code>from lzma import LZMAFile
LZMAFile(filename, 'w').write(data)
</code>

