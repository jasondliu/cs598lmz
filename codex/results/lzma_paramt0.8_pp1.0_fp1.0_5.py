from lzma import LZMADecompressor
LZMADecompressor().decompress(open('/home/user/file.lzma', 'rb').read())
</code>
It works fine.
But I received an xz (LZMA2) file. I tried this code:
<code>from lzma import LZMADecompressor
LZMADecompressor().decompress(open('/home/user/file.xz', 'rb').read())
</code>
and I got an exception 'ValueError: Inconsistent stream headers'. I tried to add <code>format=FORMAT_XZ</code> to LZMADecompressor() and it still doesn't work.
How to decipher it?
Thanks,
Pedro


A:

Use the xz module instead:
<code>&gt;&gt;&gt; import lzma
&gt;&gt;&gt; with lzma.open('test.xz', 'r') as f:
...   f.read()
</code>

