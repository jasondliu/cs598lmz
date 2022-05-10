import io
# Test io.RawIOBase subclass
try:
    from io import BytesIO as IO
except ImportError:
    from io import StringIO as IO  # python 3.x

# Test basic I/O
print("*** raw string ***")
