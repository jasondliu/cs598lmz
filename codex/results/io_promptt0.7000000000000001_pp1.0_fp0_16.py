import io
# Test io.RawIOBase
# io.RawIOBase.__init__
try:
    io.RawIOBase.__init__(mock.Mock())
except TypeError:
    pass
else:
    print('Failed')
# io.RawIOBase.read
try:
    io.RawIOBase.read(mock.Mock())
except io.UnsupportedOperation:
    pass
else:
    print('Failed')
# io.RawIOBase.readinto
try:
    io.RawIOBase.readinto(mock.Mock())
except io.UnsupportedOperation:
    pass
else:
    print('Failed')
# io.RawIOBase.write
try:
    io.RawIOBase.write(mock.Mock())
except io.UnsupportedOperation:
    pass
else:
    print('Failed')
# Test io.BufferedIOBase
# io.BufferedIOBase.__init__
try:
    io.BufferedIOBase.__init__(mock.Mock())
except TypeError:
    pass
else:
   
