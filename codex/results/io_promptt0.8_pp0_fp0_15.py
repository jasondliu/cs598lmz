import io
# Test io.RawIOBase()
try:
    io.RawIOBase()
except TypeError:
    pass
else:
    print('SKIP')
    raise SystemExit


# Test io.IOBase()
class A(io.IOBase):
    pass


try:
    A()
except TypeError:
    pass
else:
    print('SKIP')
    raise SystemExit
