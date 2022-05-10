import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f
del File

try:
    import _testcapi
except ImportError:
    _testcapi = None

def test_func():
    pass

class TestClass:
    def test_method(self):
        pass

class TestClassWithSlots:
    __slots__ = ()
    def test_method(self):
        pass

class TestClassWithDict:
    def test_method(self):
        pass

class TestClassWithWeakref:
    def test_method(self):
        pass

def test_builtin_function():
    pass

def test_builtin_method():
    pass

class TestClassWithGetattr:
    def __getattr__(self, name):
        pass

class TestClassWithGetattribute:
    def __getattribute__(self, name):
        pass

class TestClassWithGetattribute2:
    def __getattribute__(self, name):
        pass

    def __getattr__(self, name):
        pass

def test_exception():
    pass

def test
