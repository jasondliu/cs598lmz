import bz2
bz2c = bz2.BZ2Compressor()
bz2d = bz2.BZ2Decompressor()
buf = io.BytesIO()

with open(obj_meta, 'rb') as f:
    while True:
        data = f.read(io_size)
        if len(data) == 0:
            break
        buf.write(bz2c.compress(data))
        print(len(buf.getvalue()))
with open(obj_bz2, 'wb') as o:
    o.write(buf.getvalue())
    print(len(buf.getvalue()))

buf = io.BytesIO()

with open(obj_bz2, 'rb') as f:
    while True:
        data = f.read(io_size)
        if len(data) == 0:
            break
        buf.write(bz2d.decompress(data))
        print(len(buf.getvalue()))
with open(obj_meta.replace('.meta', '.meta.1'), 'wb')
