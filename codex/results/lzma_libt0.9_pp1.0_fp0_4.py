import lzma
lzma.LZMAFile(open('test', 'rb')).read()
</code>
Not only does it work, I had already done it, but looks like it doesn't decode the whole file.
I mention Lightroom because its EXIF-IO module has constants and processing code for decoding XMP and metadata.  I know it would be easier to use one of the dozens of XMP libraries out there, but I had already built the parser Decompressed XMP (in LZMA) doesn't parse in PIL (or Python) with EXIF-IO.  So it will be interesting to find a way to decode this data that's compatible with that. 
The data from one file looks like this:
<code>020000200e00000040000080200020020000
000100000006000403a80000400000000000
40000000000040000004a000000000020000
40000000000040000004a000000000020000
40000000000040000004a000000000020000
40000000000040000004a000000000020000
40000000000040000004a000000000020000
40000000000040000004a000000000020000
4
