import io
# Test io.RawIOBase

def main():
    tin = io.TextIOWrapper(io.RawIOBase(), encoding='utf-16-le')
    tout = io.TextIOWrapper(io.RawIOBase(), encoding='utf-16-be')
    tin.write('abc\nαβγ\n')
    assert tout.readline() == 'abc\n'
    assert tout.readline() == 'αβγ\n'
