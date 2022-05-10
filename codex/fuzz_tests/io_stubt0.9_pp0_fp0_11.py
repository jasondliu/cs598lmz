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
view
write(view)
'''

def test_inside_nonlocals(h):
    # check that code objects are picked up even when __code__ is buried
    # inside a nonlocal variable
    test_input = '''
def f():
    def g():
        def h():
            return 2 + 42
        return h.__code__
    h = g()
    return h

write(f())
'''
    assert h.decode(test_input) == 42
    h.decode = None

def test_inside_class(h):
    # check that code objects are picked up even when __code__ is buried
    # inside an attribute of a class instance
    #

    c = s('''
class C:
    def m(self):
        def h():
            return 2 + 1
        return h.__code__
write(C().m())
''')
    assert h.decode(c) == 42
    h.decode = None

    c = s('''
class C:
    def m(self):
       
