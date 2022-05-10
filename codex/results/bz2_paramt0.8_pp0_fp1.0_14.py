from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(msg)
</code>
First, I get this error: <code>ValueError: invalid start byte</code>.
I tried using <code>bz2.BZ2Decompressor().decompress(msg)</code> and get this other error: <code>TypeError: string argument expected, got NoneType</code>
Is there any way to decompress the file?


A:

You'll need to feed the data to the compressor, see the <code>feed()</code> method.
The <code>decompress()</code> method decompresses what it already has, <code>msg</code> is not a complete compressed file, just the compressed contents from the <code>FileReader</code>.
However, you don't need to go through all that, <code>FileReader</code> has a <code>read()</code> method that returns decompressed data directly.
<code>FileReader(file_obj=fileobj, compression=compression).read()
</code>

