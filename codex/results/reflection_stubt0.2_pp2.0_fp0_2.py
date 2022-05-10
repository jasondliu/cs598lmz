fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test that the __code__ attribute of a function can be set to a non-code object
# that has a __call__ method.
def f():
    pass

class C:
    def __call__(self):
        return 42

f.__code__ = C()
print(f())

# Test that the __code__ attribute of a function can be set to a non-code object
# that has a __call__ method, and that the function's __globals__ is used.
def f():
    return x

class C:
    def __call__(self):
        return 42

x = 1
f.__code__ = C()
print(f())

# Test that the __code__ attribute of a function can be set to a non-code object
# that has a __call__ method, and that the function's __globals__ is used.
def f():
    return x

class C:
    def __call__(self):
        return 42

x = 1
f.__code__ = C()
print(
