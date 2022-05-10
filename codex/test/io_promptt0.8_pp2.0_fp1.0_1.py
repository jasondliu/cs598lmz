import io
# Test io.RawIOBase, io.BufferedIOBase, io.TextIOBase
import io
assert isinstance(io.RawIOBase, type)
assert isinstance(io.BufferedIOBase, type)
assert isinstance(io.TextIOBase, type)
# Test io.IOBase
import io
assert isinstance(io.IOBase, type)
# Test io.BytesIO
import io
import sys
assert isinstance(io.BytesIO(), io.IOBase)
assert isinstance(io.BytesIO(), io.BufferedIOBase)
