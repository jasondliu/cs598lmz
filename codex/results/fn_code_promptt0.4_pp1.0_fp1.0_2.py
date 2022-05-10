fn = lambda: None
# Test fn.__code__
class A:
    def f(self):
        pass

def f():
    pass

print(f.__code__)
print(A.f.__code__)

# Test fn.__code__.co_consts
def f(a, b, c):
    pass

print(f.__code__.co_consts)

# Test fn.__code__.co_varnames
def f(a, b, c):
    pass

print(f.__code__.co_varnames)

# Test fn.__code__.co_argcount
def f(a, b, c):
    pass

print(f.__code__.co_argcount)

# Test fn.__code__.co_filename
def f(a, b, c):
    pass

print(f.__code__.co_filename)

# Test fn.__code__.co_firstlineno
def f(a, b, c):
    pass

print(f.__code__.co_firstlineno)
