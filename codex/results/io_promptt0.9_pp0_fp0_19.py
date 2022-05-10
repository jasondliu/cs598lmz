import io
# Test io.RawIOBase
# Use the dummy pipe-like input/output defined in test.support
with open_dummy_file('w', 10) as file:
    file.write(b'123')
    print(file.tell())
    print(file.isatty())
    file.seek(0, io.SEEK_CUR)
    file.seek(0, 0)

with open_dummy_file('rb', 10) as file:
    file.seek(5, 0)
    file.read(2)
    file.seek(0, 0)
    print(file.isatty())
    file.seek(0, io.SEEK_SET)
    file.seek(0, io.SEEK_END)
    file.seek(0, io.SEEK_CUR)


# Test io.IOBase
# Mutually recursive with test_io
# Other tests are in test_io
class NewIO(io.TextIOBase):
    pass


n = NewIO()
print(n.read())

n = NewIO()
print(bytes(byt
