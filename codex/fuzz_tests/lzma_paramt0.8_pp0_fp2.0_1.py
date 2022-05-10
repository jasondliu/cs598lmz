from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\xe0')
</code>
I think I have the right intention, but I haven't enough information to put the right formulae.
Why is this happening?


A:

The issue is in your <code>LZMADecompressor</code> object. Since you have only one instance, it is using an internal buffer to store what is left from the last decompression, and when you pass it <code>b'\xe0'</code> it thinks it is a continuation.
Just make a new instance every time.

