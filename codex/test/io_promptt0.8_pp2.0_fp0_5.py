import io
# Test io.RawIOBase

# Test constructor
reader = io.RawIOBase()
try:
    reader.fileno()
except io.UnsupportedOperation:
    pass
else:
    print("fileno() without fileno() should raise UnsupportedOperation")

