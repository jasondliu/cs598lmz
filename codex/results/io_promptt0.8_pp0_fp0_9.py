import io
# Test io.RawIOBase is a type
isinstance(io.RawIOBase, type)


class MyIO(io.RawIOBase):
    pass

# Test MyIO is also a type, despite being a subclass of RawIOBase
isinstance(MyIO, type)
# Test MyIO is not instantiable
isinstance(MyIO, type)

class MyOtherIO(io.RawIOBase):
    def read(self, *args):
        pass

# Test MyOtherIO is instantiable
x = MyOtherIO()
isinstance(x, MyOtherIO)
