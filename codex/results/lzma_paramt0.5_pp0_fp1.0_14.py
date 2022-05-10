from lzma import LZMADecompressor
LZMADecompressor().decompress(os.urandom(100))
</code>
This can be used to compress a file
<code>import lzma

with open('bigfile.txt', 'rb') as infile:
    with lzma.open('bigfile.txt.xz', 'wb') as outfile:
        outfile.write(infile.read())
</code>
and then decompress it
<code>import lzma

with lzma.open('bigfile.txt.xz') as infile:
    with open('bigfile.txt', 'wb') as outfile:
        outfile.write(infile.read())
</code>

