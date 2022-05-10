import io
# Test io.RawIOBase
from io import RawIOBase

try:
    ufunc
except NameError:
    pass # we shouldn't get here, but if we do it does
         # not implement the TODO.
else:
    # test for read/write.
    for obj in (io.IOBase, RawIOBase):
        try:
            obj().write("")
        except TypeError:
            pass
        else:
            raise Exception("%s is not abstract" % obj)

        try:
            obj().read("")
        except TypeError:
            pass
        else:
            raise Exception("%s is not abstract" % obj)

# Test io.RawIOBase.readable()
assert not io.RawIOBase().readable()

# Test io.RawIOBase.readall()
x = io.RawIOBase()
try:
    x.readall()
except io.UnsupportedOperation:
    pass
else:
    raise Exception("not UnsupportedOperation")

# Test io.RawIOBase.seekable()
assert not io.RawIOBase().seekable()

#
