from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(fK)
</code>


A:

You can try this.
<code>import bz2

with open('compressed-file-location') as f, open('uncompressed-file-location', 'wb') as w:
    decompressor = bz2.BZ2Decompressor()

    while True:
        block = f.read(100000)
        if not block:
            break
        data = decompressor.decompress(block)
        if not data:
            break
        w.write(data)

    w.write(decompressor.flush())
</code>
Read while the stream got data and write data into file.

