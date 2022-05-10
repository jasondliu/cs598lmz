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

class T:
    def __del__(self):
        del view

T()

"""

def test_bug_13712(pyc):
    pyc.py_exec(SCRIPT)
    del pyc


SCRIPT = """if 1:
    def f1(a):
        assert a == 'hello'
        return a

    def f2(a, b=None):
        assert a == 'hello'
        assert b == 'world'
        return a, b

    def f3(a, b=None, c=None):
        assert a == 'hello'
        assert b == 'world'
        assert c == 'foo'
        return a, b, c

    def f4(a, b=None, c=None, d=None):
        assert a == 'hello'
        assert b == 'world'
        assert c == 'foo'
        assert d == 'bar'
        return a, b, c, d

    def f5(a, b=None, c=None, d=None, e=None):
        assert
