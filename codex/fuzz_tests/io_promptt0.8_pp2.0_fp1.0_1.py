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
assert isinstance(io.BytesIO(), io.RawIOBase)
assert not isinstance(io.BytesIO(), io.TextIOBase)
# Test io.StringIO
import io
import sys
assert isinstance(io.StringIO(), io.IOBase)
assert isinstance(io.StringIO(), io.BufferedIOBase)
assert isinstance(io.StringIO(), io.TextIOBase)
assert not isinstance(io.StringIO(), io.RawIOBase)
# Test io.FileIO
import io
import sys
assert isinstance(io.File
