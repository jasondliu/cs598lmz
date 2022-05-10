from types import FunctionType
list(FunctionType(lambda: 0, {}, None, None, None))
# list(lambda: 0)

class A(object):
    def __init__(self, x):
        self.x = x
    def __getitem__(self, y):
        return self.x + y
    def __len__(self):
        return self.x
    def __call__(self):
        return self.x

a = A(1)
list(a)

class B(object):
    def __init__(self, x):
        self.x = x
    def __getitem__(self, y):
        return self.x + y
    def __len__(self):
        return self.x
    def __call__(self):
        return self.x

b = B(1)
list(b)

class C(object):
    def __init__(self, x):
        self.x = x
    def __getitem__(self, y):
        return self.x + y
    def __len__(self):
        return self.
