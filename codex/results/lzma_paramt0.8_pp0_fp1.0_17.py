from lzma import LZMADecompressor
LZMADecompressor(format=FORMAT_ALONE).decompress(data)
# b'12345abcde\n'
</code>
or if you want to write to a file:
<code>from lzma import LZMAFile
with LZMAFile(fileobj) as f:
    f.write(data)
</code>

