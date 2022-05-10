from lzma import LZMADecompressor
LZMADecompressor().decompress(input)
</code>
Now, I would like to decompress in pieces, similar to how the <code>.read(size)</code> function works with regular files.
It is possible to do this with LZMA files?
I've been trying to use xz-utils, with <code>xz -d -c -T0 &lt; filename.xz &gt; /dev/null</code>. But I noticed the output is corrupted (seems the decompressor adds some extra bytes).


A:

xz does not need to decompress a whole file to start reading the data. It reads the blocks in the needed order. Unfortunately xz does not have a Python API.
It might be possible to implement a Python API for xz with a bit of work.

