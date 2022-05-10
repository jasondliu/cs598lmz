import io
# Test io.RawIOBase()
import io

if hasattr(io, "RawIOBase"):
    print(issubclass(io.RawIOBase, object))

# Test io.BufferedIOBase()
import io

if hasattr(io, "BufferedIOBase"):
    print(issubclass(io.BufferedIOBase, object))

# Test io.TextIOBase()
import io

if hasattr(io, "TextIOBase"):
    print(issubclass(io.TextIOBase, object))

# Test io.FileIO()
import io

if hasattr(io, "FileIO"):
    print(issubclass(io.FileIO, object))

# Test io.StringIO()
import io

if hasattr(io, "StringIO"):
    print(issubclass(io.StringIO, object))

# Test io.BytesIO()
import io

if hasattr(io, "BytesIO"):
    print(issubclass(io.BytesIO, object))
