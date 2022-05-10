import io
# Test io.RawIOBase
try:
    # io.RawIOBase implements readline() and write()
    io.RawIOBase().readline()
    io.RawIOBase().write(b'')
except io.UnsupportedOperation:
    io.RawIOBase = object

# Test io.BufferedIOBase
try:
    # io.BufferedIOBase implements read() and write()
    io.BufferedIOBase().read(0)
    io.BufferedIOBase().write(b'')
except io.UnsupportedOperation:
    io.BufferedIOBase = io.RawIOBase

# Test io.TextIOBase
try:
    # io.TextIOBase implements read() and write()
    io.TextIOBase().read(0)
    io.TextIOBase().write('')
except io.UnsupportedOperation:
    io.TextIOBase = io.RawIOBase
# Patch text-specific methods
for name in ('readline', 'readlines', 'writelines'):
    try:
        getattr(io.TextIOBase, name)
    except AttributeError:
