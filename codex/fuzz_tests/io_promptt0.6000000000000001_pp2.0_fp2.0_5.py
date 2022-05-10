import io
# Test io.RawIOBase
try:
    io.RawIOBase
except:
    pass
else:
    raise TestFailed("io.RawIOBase defined when it shouldn't be")

# Test io.BufferedIOBase
try:
    io.BufferedIOBase
except:
    pass
else:
    raise TestFailed("io.BufferedIOBase defined when it shouldn't be")

# Test io.TextIOBase
try:
    io.TextIOBase
except:
    pass
else:
    raise TestFailed("io.TextIOBase defined when it shouldn't be")

# Test io.FileIO
try:
    io.FileIO
except:
    pass
else:
    raise TestFailed("io.FileIO defined when it shouldn't be")

# Test io.BytesIO
try:
    io.BytesIO
except:
    pass
else:
    raise TestFailed("io.BytesIO defined when it shouldn't be")

# Test io.StringIO
try:
    io.StringIO
except:
    pass
else:
    raise TestFailed
