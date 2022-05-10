from bz2 import BZ2Decompressor
BZ2Decompressor().decompress()
</code>
The last line gives above error, which is quite strange. Is there a way to decompress the .bz2 file?


A:

You need to feed data into the decompressor.
<code>with open(path, 'rb') as f:
    decomp = BZ2Decompressor()
    for chunk in iter(lambda: f.read(100 * 1024), b''):
        data = decomp.decompress(chunk)
        if data: break  # or whatever you do with decompressed input
</code>

