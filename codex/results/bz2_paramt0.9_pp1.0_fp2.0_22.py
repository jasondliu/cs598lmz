from bz2 import BZ2Decompressor
BZ2Decompressor().decompress("\x42\x5a\xff\xff")
# b'\x59\xf0'
</code>
What's going on? Where did my last four bytes go? It says it read <code>b'\x42\x5a\xff\xff'</code>, yet the output has no relation to the input.


A:

You forgot that <code>b'\x42\x5a\xff\xff'</code> is three bytes: the character <code>B</code>, the character <code>Z</code>, and the byte <code>\xff</code>. BZ2 compression is a byte-stream compression algorithm, and it works in a sliding window. A simple BZ2 stream is completely out-of-order. If you begin with a BZ2 compressed file that ends in <code>\xff</code>, and then append more data, then the final output is the same as if you just BZ2 compressed the new data, appended the new data to the original compressed data, and then uncompressed the whole appended block.
To test this, I created three text files:


