from types import FunctionType
list(FunctionType(lambda: None, globals()))

# Test that __repr__ is not called
class A:
    def __repr__(self):
        raise Exception

a = A()
list(a)

# Test that __len__ is not called
class B:
    def __len__(self):
        raise Exception

b = B()
list(b)

# Test that __iter__ is not called
class C:
    def __iter__(self):
        raise Exception

c = C()
list(c)

# Test that __getitem__ is not called
class D:
    def __getitem__(self, i):
        raise Exception

d = D()
list(d)

# Test that __getitem__ is not called
class E:
    def __getitem__(self, i):
        if i == 0:
            raise Exception
        else:
            raise StopIteration

e = E()
list(e)

# Test that __getitem__ is not called
class F:
    def __getitem__(self
