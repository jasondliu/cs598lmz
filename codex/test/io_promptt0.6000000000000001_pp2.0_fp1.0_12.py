import io
# Test io.RawIOBase.readinto()

import _io

try:
    _io.BytesIO
except AttributeError:
    import io
    _io = io

