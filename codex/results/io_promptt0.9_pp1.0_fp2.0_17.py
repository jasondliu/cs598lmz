import io
# Test io.RawIOBase

def main():
    tin = io.TextIOWrapper(io.RawIOBase(), encoding='utf-16-le')
    tout = io.TextIOWrapper(io.RawIOBase(), encoding='utf-16-be')
    tin.write('abc\nαβγ\n')
    assert tout.readline() == 'abc\n'
    assert tout.readline() == 'αβγ\n'
    with io.TextIOWrapper(io.BytesIO(b"abc\nαβγ\n"), encoding='utf-16-le') as tin:
        with io.TextIOWrapper(io.BytesIO(), encoding='utf-16-be') as tout:
            tout.write(tin.readline())
            tout.write(tin.readline())
    with io.TextIOWrapper(io.BytesIO(b'abc\nαβγ\n'), encoding='utf-16-le') as tin:
        with io.TextIOWrapper(io.BytesIO(), encoding='utf-16-
