from lzma import LZMADecompressor
LZMADecompressor().decompress(file)
</code>
But this seems to give me some bytes that are not utf-8 encoded, and throw the following exception:
<code>UnicodeDecodeError: 'utf-8' codec can't decode byte 0x0a in position 376: invalid start byte
</code>
When I look at the error and into the bytes, I notice that a lot of the lines begin with <code>0x0a</code>, I assume that this is because of where the line ends, and possibly also the encoding, but I'm not sure. 
It's worth noting that all the lines in the file are sentences, and the file is (in my dataset) around 9MB.
So my question: How do I properly encode this file after decompression?


A:

If you look at the source you'll see that the decompressor returns a <code>bytearray</code>.
<code>bytearrays</code> are sequences of integer values <code>0-255</code>, so they're not encoding specific, no matter what Python thinks. You're seeing bytes, nothing more.
Convert this to a <
