import io
# Test io.RawIOBase
try:
    a = io.RawIOBase()
    a.read(0)
    a.close()
    a.isatty()
    a.readinto1(b'de')
    a.readall()
# Forbiden
except TypeError:
    print()
except AttributeError:
    print()
#>>
