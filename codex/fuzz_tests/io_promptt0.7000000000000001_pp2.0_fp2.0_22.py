import io
# Test io.RawIOBase
with open('a', 'w'):
    pass

with open('a', 'r'):
    pass

with open('a', 'r+'):
    pass

with open('a', 'rw'):
    pass

with open('a', 'rw+'):
    pass

with open('a', 'a+'):
    pass

with open('a', 'w+'):
    pass

# Test io.BufferedIOBase
with io.BytesIO():
    pass

with io.StringIO():
    pass

# Test io.TextIOBase
with io.StringIO():
    pass

with io.StringIO():
    pass

# Test io.TextIOWrapper
with io.StringIO():
    pass

with io.StringIO():
    pass

# Test io.BytesIO
with io.BytesIO():
    pass

# Test io.FileIO
with io.FileIO('a', 'w'):
    pass

# Test io.BufferedReader
with io.BytesIO():
    pass
