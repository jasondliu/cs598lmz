from lzma import LZMADecompressor
LZMADecompressor.decompress(data).decode('utf-8')
</code>
This is my code
<code>from lzma import LZMADecompressor
import io

with io.BytesIO() as tbuf:
    tbuf.write(data)
    tbuf.seek(0)
    LZMADecompressor().decompress(tbuf).decode('utf-8')
</code>
but this gives TypeError: must be XZ-compressed data

