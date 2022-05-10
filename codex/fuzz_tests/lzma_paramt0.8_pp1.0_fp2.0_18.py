from lzma import LZMADecompressor
LZMADecompressor().decompress(file)
</code>
The error is:
<code>ValueError: incomplete or unkown stream type
</code>
The file is an LZMA file. How can I fix this?


A:

The lzma module can read LZMA files, but that file is a LZO file (it starts with <code>\x89LZO</code>).
You can use the lzo module for this instead (the project site is at http://www.oberhumer.com/opensource/lzo/). For example:
<code>import lzma
import lzo.decompress
import lzo.version

data = '\x89LZO\x00\x00\x00\x1D\xf3\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00Hello World\x00'

print('LZO version: ', lzo.version)
print('LZO data is size = ', len(
