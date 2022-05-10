import io
# Test io.RawIOBase
try:
    io.RawIOBase()
except TypeError:
    pass
else:
    print('ERROR: expected TypeError')
# Test io.RawIOBase.readinto()
try:
    io.RawIOBase().readinto(bytearray())
except NotImplementedError:
    pass
else:
    print('ERROR: expected NotImplementedError')
# Test io.RawIOBase.write()
try:
    io.RawIOBase().write(b'')
except NotImplementedError:
    pass
else:
    print('ERROR: expected NotImplementedError')
# Test io.RawIOBase.read()
try:
    io.RawIOBase().read()
except NotImplementedError:
    pass
else:
    print('ERROR: expected NotImplementedError')
