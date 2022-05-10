import io
# Test io.RawIOBase.seekable
infile = open(__file__, "r")
assert infile.seekable() == True
infile.close()
try:
    class MySeekable(io.RawIOBase):
        def seekable(self, *args):
            return False
    raise BaseException()
except TypeError:
    pass
try:
    class MySeekable(io.RawIOBase):
        def seekable(self, *args):
            return True
    MySeekable().seekable(False)
    raise BaseException()
except TypeError:
    pass
try:
    class MySeekable(io.RawIOBase):
        def seekable(self, *args):
            return [1, 2, 3]
    MySeekable().seekable()
    # Can't catch return type, as it's a duck typing check
except Exception as e:
    pass
class MySeekable(io.RawIOBase):
    def seekable(self, *args):
        return True
print(MySeekable().seekable())

# Test io.Raw
