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
convert_to_str(view)

# __new__
class A(object):
    def __new__(*args):
        return "abc"

a = A()

# __init__
class B(object):
    def __init__(self, val):
        global view
        view = val

b = B("def")
convert_to_str(view)

# __init__, with __new__
class C(object):
    def __new__(*args):
        return "xyz"
    def __init__(self, val):
        self.val = val

c = C("ghi")
convert_to_str(c.val)

# __init__, with __new__
class D(object):
    def __new__(*args):
        return "xyz"
    def __init__(self, val):
        print(val)

d = D("ghi")

# __call__
class E(object):
    def __call__(self, val):
        global view
        view =
