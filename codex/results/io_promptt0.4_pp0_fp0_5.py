import io
# Test io.RawIOBase
# Test io.BufferedIOBase
# Test io.IOBase
# Test io.TextIOBase

# Test io.FileIO
with open('README.md', 'r') as f:
    print(f.read())

# Test io.BytesIO
b = io.BytesIO()
b.write(b'Hello World')
print(b.getvalue())

# Test io.StringIO
s = io.StringIO()
s.write('Hello World')
print(s.getvalue())

# Test io.TextIOWrapper
with open('README.md', 'r', encoding='utf-8') as f:
    print(f.read())

# Test io.open
with io.open('README.md', 'r', encoding='utf-8') as f:
    print(f.read())

# Test io.BytesIO
with io.BytesIO() as b:
    b.write(b'Hello World')
    print(b.getvalue())

# Test io.StringIO
with io.StringIO() as s:
