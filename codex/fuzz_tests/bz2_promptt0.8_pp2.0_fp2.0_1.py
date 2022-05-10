import bz2
# Test BZ2Decompressor (does not provide a functional BZ2Decompressor object)

filename = 'empty.txt.bz2'
f = bz2.BZ2File(filename)
decomp = bz2.BZ2Decompressor.decompress(f.read())
decomp

# This is the expected output:
# b''

# The following is the actual output:
# b'BZh9\xcd\xcb\xd8\xe1\x02\x00\x1d\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
</code>
It seems from the above that the <code>bz2.BZ2Decompressor.decompress()</code> method does not decompress the file.
The following code does decompress the file.
<code>import bz2
# Test BZ2Decompressor

filename = 'empty.txt.bz2'
f = bz2.BZ2File(filename)
decompress
