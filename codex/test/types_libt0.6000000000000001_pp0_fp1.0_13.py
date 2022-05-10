import types
types.SimpleNamespace

class A:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


a = A(1, 2, 3)
a.x, a.y, a.z


class B:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f'B(x={self.x}, y={self.y}, z={self.z})'


b = B(1, 2, 3)
b


class C:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


c = C(x=1, y=2, z=3)
c.x, c.y, c.z


class D:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

