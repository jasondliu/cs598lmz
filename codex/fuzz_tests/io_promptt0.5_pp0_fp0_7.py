import io
# Test io.RawIOBase

import _io

# test RawIOBase constructor
try:
    _io.RawIOBase()
except TypeError:
    pass
else:
    print('TypeError expected')

# test RawIOBase read()
try:
    _io.RawIOBase().read()
except NotImplementedError:
    pass
else:
    print('NotImplementedError expected')

# test RawIOBase readinto()
try:
    _io.RawIOBase().readinto(bytearray(1))
except NotImplementedError:
    pass
else:
    print('NotImplementedError expected')

# test RawIOBase readall()
try:
    _io.RawIOBase().readall()
except NotImplementedError:
    pass
else:
    print('NotImplementedError expected')

# test RawIOBase write()
try:
    _io.RawIOBase().write(b'')
except NotImplementedError:
    pass
else:
    print('NotImplementedError expected')

# test Raw
