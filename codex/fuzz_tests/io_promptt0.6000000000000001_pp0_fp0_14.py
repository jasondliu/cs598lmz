import io
# Test io.RawIOBase
try:
    io.RawIOBase().read()
except TypeError:
    pass
else:
    print('FAILED: expected TypeError')

# Test io.BufferedIOBase
try:
    io.BufferedIOBase().read()
except TypeError:
    pass
else:
    print('FAILED: expected TypeError')

# Test io.TextIOBase
try:
    io.TextIOBase().read()
except TypeError:
    pass
else:
    print('FAILED: expected TypeError')

# Test io.FileIO
try:
    io.FileIO().read()
except TypeError:
    pass
else:
    print('FAILED: expected TypeError')

# Test io.BytesIO
try:
    io.BytesIO().read()
except TypeError:
    pass
else:
    print('FAILED: expected TypeError')

# Test io.StringIO
try:
    io.StringIO().read()
except TypeError:
    pass
else:
    print('FAILED: expected Type
