import lzma
lzma.LZMAFile(fileobj=fs, format=lzma.FORMAT_AUTO, mode='rb')
</code>
That raises an exception:
<code>lzma.LZMAError: LZMA decoding error: Corrupted input
</code>
How to decompress both tar and lzma from the following content?
<code>import os
fs = open("{}.tar.gz.lzma".format(os.path.splitext(PATH)[0]), 'rb')
lzma.LZMAFile(fileobj=fs, format=lzma.FORMAT_AUTO, mode='rb')
</code>

