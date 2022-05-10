from lzma import LZMADecompressor
LZMADecompressor().decompress(r.content)
</code>
But this gives the error:
<code>LZMAError: LZMAError: Error in the LZMA stream
</code>
I've changed the expected blocksize from 1MB to 16MB and it says the file is corrupt.
I've also tried xzcat but that says the file is corrupt.
I've tried opening the file in PHP but it also says the file is corrupt.
The file can be opened in 7zip so I know that the file is not corrupt.
Anyone have any ideas?


A:

I had a similar issue, and it turns out that the stream is not only the LZMA stream but also the appended archive data.
The easiest way to get around this is to use the Python xzfile module.
<code>from xzfile.xzfile import open as xzopen

r = requests.get(url)
xz = xzopen(r.content)
print(xz.read())
</code>
The other way is to first decompress the LZMA stream and then read the resulting archive:
<code>
