import bz2
# Test BZ2Decompressor.
for i in range(1, 10):
    bz2_decompressor = bz2.BZ2Decompressor()
    data = bz2_decompressor.decompress(bz2_data)
    print(len(data))
    bz2_decompressor.decompress(b'BZh91')
    bz2_decompressor.decompress(b'BZh91')
    bz2_decompressor.decompress(b'BZh91')
    bz2_decompressor.decompress(b'BZh91')
    bz2_decompressor.decompress(b'BZh91')
</code>
The above code works fine, but the following code does not work:
<code># Test BZ2Decompressor.
for i in range(1, 10):
    bz2_decompressor = bz2.BZ2Decompressor()
    data = bz2_decompressor.decompress(bz2_data)
    print(
