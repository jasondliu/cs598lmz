from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)
</code>
or, if you want to do it all in one go:
<code>with open(filename, 'rb') as f:
    print(BZ2Decompressor().decompress(f.read()))
</code>

