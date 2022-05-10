from lzma import LZMADecompressor
LZMADecompressor().decompress(compressed_data)
</code>
The output I get is: "foo bar baz"
There is some similarity in the output of <code>zlib.compress</code> and <code>lzma.compress</code>, but I am not sure on what the similarity is based, or how to convert the output of Zlib to something useful to LZMA.


A:

<code>lzma</code> has a function to decompress data compressed with <code>zlib</code>; it is called <code>compress_from_zlib</code>:
<code>&gt;&gt;&gt; from lzma import compress, compress_from_zlib
&gt;&gt;&gt; compress(b'foo bar baz')
b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x1c\x00\x00\x00t/\xe5\xa3\x01\x00\x00\x00'
