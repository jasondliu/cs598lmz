import ctypes
ctypes.cast(0, ctypes.py_object)


class C:
    def __init__(self):
        self.data = 0

    def __repr__(self):
        return '<C %s>' % self.data

c = C()
c
c.data = 'hello'
c
c.data = 1
c

class D:
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return '<D %s>' % self.data

d = D(1)
d
D('hello')
D(3.14)
D([1, 2, 3])
D({'a': 1, 'b': 2})

class E:
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return '<E %s>' % self.data

    def __add__(self, other):
        return E(self.data + other.data)

