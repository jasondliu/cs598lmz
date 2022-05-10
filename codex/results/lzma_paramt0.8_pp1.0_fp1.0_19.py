from lzma import LZMADecompressor
LZMADecompressor().decompress(compressed)
# 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
</code>
To decompress a whole file, you need to read it in little by little and give each chunk to the decompressor object, since it doesn't know when the end of the stream is:
<code>with open('compressed.xz', 'rb') as f:
    decompressor = LZMADecompressor()
    for chunk in iter(lambda: f.read(1024 * 1024), b''):
        decompressor.decompress(chunk)
decompressed = decompressor.flush()
</code>

There's also a <code>open</code> function that works like the built-in <code>open</code>, but decompresses for you as you read, and a <code>Compressor</code> class for doing the inverse.

