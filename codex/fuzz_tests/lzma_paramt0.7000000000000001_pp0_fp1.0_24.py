from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

...

# Decompress a file
from lzma import LZMAFile
with LZMAFile('foo.xz', 'rb') as f:
    file_content = f.read()
</code>

