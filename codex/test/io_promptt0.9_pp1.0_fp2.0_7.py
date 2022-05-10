import io
# Test io.RawIOBase
# Test __init__()
try:
    io.RawIOBase()
except TypeError:
    pass
