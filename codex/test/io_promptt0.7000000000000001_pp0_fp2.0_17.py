import io
# Test io.RawIOBase
try:
    print(io.RawIOBase.__name__)
    print(io.RawIOBase.readinto)
    print(io.RawIOBase.readinto.__doc__)
except:
    print("SKIP")

# Test io.BufferedIOBase
try:
    print(io.BufferedIOBase.__name__)
    print(io.BufferedIOBase.peek)
    print(io.BufferedIOBase.peek.__doc__)
except:
    print("SKIP")

# Test io.BytesIO
try:
    print(io.BytesIO.__name__)
    print(io.BytesIO.getvalue)
    print(io.BytesIO.getvalue.__doc__)
except:
    print("SKIP")

# Test io.StringIO
try:
    print(io.StringIO.__name__)
    print(io.StringIO.getvalue)
    print(io.StringIO.getvalue.__doc__)
except:
    print("SKIP")

# Test
