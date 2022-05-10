import io
# Test io.RawIOBase
# Write a few bytes
with io.BytesIO() as f:
    f.write(b'abc')
    f.seek(0)
    assert f.read() == b'abc'
# Test io.BufferedIOBase
# Write a few bytes
with io.BytesIO() as f:
    f.write(b'abc')
    f.seek(0)
    assert f.read() == b'abc'
# Test io.TextIOBase
# Write a few bytes
with io.StringIO() as f:
    f.write('abc')
    f.seek(0)
    assert f.read() == 'abc'
# Test io.IOBase
# Write a few bytes
with io.StringIO() as f:
    f.write('abc')
    f.seek(0)
    assert f.read() == 'abc'
# Test io.FileIO
# Write a few bytes
with io.FileIO('io_test.txt', 'w+') as f:
    f.write(b'abc')
    f.seek(0)
   
