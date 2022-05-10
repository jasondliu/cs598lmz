import bz2
# Test BZ2Decompressor

def assert_eq(a, b):
    if a != b:
        raise AssertionError 
    return True

def assert_eq_with_none(a, b):
    assert_eq(a is None, b is None)
    if a is not None:
        assert_eq(a, b)

def input_chunks(x):
    yield x[:len(x)//2]
    yield x[len(x)//2:]

def input_chunks_multi(x):
    n = 2
    while n < len(x):
        yield x[:n]
        n *= 2

def input_chunks_empty(x):
    yield b""
    yield x

def test_decompressor_state(x):
    c = bz2.BZ2Decompressor()
    res = b""
    for chunk in input_chunks(x):
        res += c.decompress(chunk)
    res += c.flush()
    return res

