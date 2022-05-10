from types import FunctionType
list(FunctionType(lambda x: x+1, globals(), 'foo')(1))

class A:
    def __init__(self, x):
        self.x = x
    def __getitem__(self, i):
        return self.x + i
a = A(1)
list(a[1:])

class B:
    def __init__(self, x):
        self.x = x
    def __getitem__(self, i):
        return self.x + i
    def __len__(self):
        return 10
b = B(1)
list(b[1:])

class C:
    def __init__(self, x):
        self.x = x
    def __getitem__(self, i):
        return self.x + i
    def __len__(self):
        return 10
c = C(1)
list(c[1:11])

class D:
    def __init__(self, x):
        self.x = x
    def __getitem__(self, i):
        return
