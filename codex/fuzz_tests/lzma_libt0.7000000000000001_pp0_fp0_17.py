import lzma
lzma = lzma.__file__


def _lzma_compress(data):
    with lzma.open(BytesIO(data), 'w', format=lzma.FORMAT_RAW) as f:
        f.write(data)
    return f.tell()


def _lzma_decompress(data):
    with lzma.open(BytesIO(data), 'r', format=lzma.FORMAT_RAW) as f:
        return f.read()


def _lzma_serialize(data):
    data = pickle.dumps(data)
    i = _lzma_compress(data)
    return pickle.dumps((i, data))


def _lzma_deserialize(se, version=None):
    i, data = pickle.loads(se)
    s = _lzma_decompress(data)
    assert len(s) == i
    return pickle.loads(s)


def serialize(data, version=None):
    return _lz
