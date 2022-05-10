from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda'))

# code objects
def f(x):
    return x
list(f.__code__)

# method-wrapper objects
class C:
    def f(self):
        pass
list(C.f)

# wrapper_descriptor objects
class C:
    def f(self):
        pass
list(C.__dict__['f'])

# method-wrapper objects
class C:
    def f(self):
        pass
list(C().__dict__['f'])

# method-wrapper objects
class C:
    def f(self):
        pass
list(C().f)

# member_descriptor objects
class C:
    def f(self):
        pass
list(C.f)

# getset_descriptor objects
class C:
    def __init__(self):
        self.x = 1
list(C.__dict__['x'])

# member_descriptor objects
class C:
    def __init__(self):

