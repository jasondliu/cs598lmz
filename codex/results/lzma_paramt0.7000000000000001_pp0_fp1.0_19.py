from lzma import LZMADecompressor
LZMADecompressor().decompress(response.content)

import lzma
with lzma.open('content.zip') as f:
    file_content = f.read()

file_content
</code>


A:

You're trying to uncompress a gzip file with <code>LZMADecompressor</code> try using the <code>GzipFile</code> class.
<code>import gzip
import StringIO

s = StringIO.StringIO(response.content)
gzip_file = gzip.GzipFile(fileobj=s)
file_content = gzip_file.read()
</code>

