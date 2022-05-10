import lzma
lzma.LZMACompressor(format=lzma.FORMAT_XZ, check=lzma.CHECK_SHA256, preset=9).compress(open('test.txt', 'rb').read())
</code>
I'm not sure if there's a better way to do this, but this seems to work.

