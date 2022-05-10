import io
# Test io.RawIOBase
# TODO: io.RawIOBase
# TODO: io.BufferedIOBase
# TODO: io.BytesIO
# TODO: io.StringIO
# TODO: io.TextIOBase
# TODO: io.FileIO
# TODO: io.BytesIO

# Test io.StringIO
f = io.StringIO()
f.write('hello')
print(f.getvalue())

f = io.StringIO('hello, world')
print(f.read())

# Test io.BytesIO
f = io.BytesIO()
f.write(u'你好'.encode('utf-8'))
print(f.getvalue())

f = io.BytesIO('你好'.encode('utf-8'))
print(f.read())

# Test io.TextIOWrapper
f = io.StringIO('hello, world')
print(f.read())

f = io.TextIOWrapper(io.StringIO('hello, world'), encoding='utf-8')
