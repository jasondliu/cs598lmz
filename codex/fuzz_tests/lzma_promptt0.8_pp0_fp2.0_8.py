import lzma
# Test LZMADecompressor on its own.
d = lzma.LZMADecompressor()

d.decompress(b'\x00')
d.decompress(b'\xff')

def make_data():
    data = io.BytesIO()
    data.write(b'BEGIN')
    for i in range(10000):
        data.write(b'XXXXXXXX')
    data.write(b'END')
    data.seek(0)
    return data.read()

def make_xz_data(data):
    xz = io.BytesIO()
    with lzma.open(xz, 'w') as fo:
        fo.write(data)
    xz.seek(0)
    return xz.read()


def test_halfway_xz_data():
    # The decompressor should decompress part of the stream and then
    # wait for more data to come in.
    data = make_data()
    decompressor = lzma.LZMADecompressor()
    xzdata = make_xz
