import lzma
# Test LZMADecompressor class is compatible with the
# lzma.LZMAFile class

def test_decompress():
    with lzma.open('data/example.xz', 'rb') as f:
        data = f.read()
    assert data == b'This is a test file.\n' * 10

def test_decompress_to_file():
    with lzma.open('data/example.xz', 'rb') as f:
        with open('/tmp/example', 'wb') as out:
            data = f.read(10)
            while data:
                out.write(data)
                data = f.read(10)
    with open('/tmp/example', 'rb') as f:
        data = f.read()
    assert data == b'This is a test file.\n' * 10

