from lzma import LZMADecompressor
LZMADecompressor().decompress(file.read())
</code>
I get an error. It says:
<code>decompress() argument 1 must be string or buffer, not TemporaryFile
</code>
How can I fix this?


A:

It seems like you are using an older version of <code>lzma</code>.
<code>from lzma import LZMADecompressor
from tempfile import TemporaryFile

compressed = TemporaryFile()
compressed.write(b"&lt;compressed data&gt;")

decompressor = LZMADecompressor()
decompressed = decompressor.decompress(compressed.read())

print(decompressed)
</code>

