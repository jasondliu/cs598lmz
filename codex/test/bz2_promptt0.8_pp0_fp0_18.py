import bz2
# Test BZ2Decompressor
def read_file(filename):
    with bz2.BZ2File(filename) as first_file, bz2.BZ2File(filename) as second_file:
        assert first_file.read() == second_file.read()

read_file('test.bz2')
