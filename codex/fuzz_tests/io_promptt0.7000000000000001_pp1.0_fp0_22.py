import io
# Test io.RawIOBase
# Test io.BufferedIOBase
# Test io.TextIOBase
# Test io.IOBase
# Test io.FileIO
# Test io.BytesIO
f = io.FileIO(b'xyz.txt')
f.close()
f = io.BytesIO()
f.close()
f = io.BytesIO(b'abcdefg')
f.getvalue()
f.close()
f = io.BytesIO(b'abcdefg')
f.read()
f.close()
f = io.BytesIO(b'abcdefg')
f.readline()
f.close()
f = io.BytesIO(b'abcdefg')
f.readlines()
f.close()
f = io.BytesIO()
f.write(b'abcdefg')
f.getvalue()
f.close()
f = io.BytesIO()
f.writelines([b'abc', b'defg'])
f.getvalue()
f.close()
# Test io.StringIO
f = io.StringIO()
f.close()
