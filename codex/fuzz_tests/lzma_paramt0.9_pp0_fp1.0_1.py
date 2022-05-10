from lzma import LZMADecompressor
LZMADecompressor().decompress(f)

for line in f:
    print(line)
</code>


A:

With a <code>BytesIO</code>, you don't get a random access file, but a sequence of bytes.
If you want to use <code>seek()</code>, you have to use a regular <code>open()</code>, with the appropriate mode, e.g. <code>"rb"</code>.

