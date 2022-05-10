import lzma
# Test LZMADecompressor on the above stream
decompressor = lzma.LZMADecompressor()
try:
    data = decompressor.decompress(b'\x00' * (1 << 23) + encoded)
    # Decompressor managed to handle the data,
    # so it wasn't truncated.
except lzma.LZMAError:
    # Data was truncated, decompressor couldn't
    # find eos marker.
    pass
# ... but what is the original object?
def decompress_via_iter(lzmaobj, x):
    l = ['x'] * x
    for char in lzmaobj.decompress(l):
        yield char
joined_data = b''.join(decompress_via_iter(decompressor, x))
data == joined_data

</code>


A:

If you compare the uncompressed data bytes, you'll see they are identical.
Using <code>print(x.decode('utf-8'))</code> on your <code>joined_data</code> should also work fine.

