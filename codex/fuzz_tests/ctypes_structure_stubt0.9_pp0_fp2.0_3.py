import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double(2.0)
s = S()
print('hello', s.x)
s.x = s.x / 5.0
print('hello', s.x)

# make a function invocation
print(1.0 * 2.0 + 3.0)

# create a class with a pure virtual method
class V(metaclass=ABCMeta):
    @abstractmethod
    def foo(self):
        return 0
try:
    v = V()
except TypeError:
    pass

# create a class with a pure virtual method, override in the derived class
class V(metaclass=ABCMeta):
    @abstractmethod
    def foo(self):
        return 0
class U(V):
    def foo(self):
        return 1
u = U()
assert(u.foo() == 1)

# get a module global
print(gctest.PY_SSIZE_T_CLEAN)

# try to close a file
f = open(__file__, 'r')
f.close()

# create
