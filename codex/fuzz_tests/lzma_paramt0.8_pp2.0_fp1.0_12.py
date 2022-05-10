from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\x00\xff\xff')
</code>
But using <code>xz</code> the code works.
<code>$ echo '\x00\xff\xff' | xxd -r | xz -d

$
</code>
I think that the problem is related to End of Payload Mark (EOPM) but I couldn't find a way to make <code>lzma.LZMADecompressor</code> work.

