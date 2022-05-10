from lzma import LZMADecompressor
LZMADecompressor().decompress(data)
# b'This is the text.'
</code>
And, of course, you can use <code>xz</code> from the command line:
<code>$ echo "This is the text." | xz -9 --format=lzma | xz -d
This is the text.
</code>

