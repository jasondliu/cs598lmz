import lzma
# Test LZMADecompressor with multiple buffers
decomp = lzma.LZMADecompressor()
with open(sys.argv[1],"rb") as f:
    while True:
        block = f.read(5)
        if not block:
            break
        print ("Input: %r" % block)
        dec = decomp.decompress(block)
        print ("Output: %r" % dec)
dec = decomp.flush()
print ("Final output: %r" % dec)
print ("Output length: %d" % len(dec))
</code>
You can see from the output below that the decompressor processes the input in chunks of 5 bytes at a time and produces different output. The decompressed size is reported as 534 bytes when decompressing the entire input in one go, but when you do it in chunks of 5 bytes you get 536 bytes (you can see the last 2 bytes are not "flushed" until the final <code>flush()</code> call).
<code>python test.py test.xz
Input: b'&lt;\x9c\xa6\x8b'
Output
