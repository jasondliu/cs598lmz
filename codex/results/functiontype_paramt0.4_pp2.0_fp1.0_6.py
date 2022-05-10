from types import FunctionType
list(FunctionType(lambda: None, globals()))

class A:
    def __init__(self, x):
        self.x = x
    def __iter__(self):
        return self
    def __next__(self):
        if self.x == 0:
            raise StopIteration
        self.x -= 1
        return self.x

list(A(5))

class B:
    def __init__(self, x):
        self.x = x
    def __iter__(self):
        return self
    def __next__(self):
        if self.x == 0:
            raise StopIteration
        self.x -= 1
        return self.x
    def __getitem__(self, x):
        return x

list(B(5))

class C:
    def __init__(self, x):
        self.x = x
    def __iter__(self):
        return self
    def __getitem__(self, x):
        if x == 0:
            raise StopIteration
        self.x -= 1

