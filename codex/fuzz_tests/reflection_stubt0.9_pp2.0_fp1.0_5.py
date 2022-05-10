fn = lambda: None
gi = (i for i in ())
fn.__code__ = lambda: gi
next(fn())

# fn.__code__.__code__ on CPython
fn = lambda: None
fn.__code__ = type(fn.__code__)(b'')
fn()

# fn.__code__.__code__ on PyPy
fn = (lambda: None).__code__
fn.co_code = 0
fn()

# fn.__call__ on CPython
def f():
    return 0


# a = f.__call__
# def g():
#     a()
# g()

# __class__ on CPython
a = {}
# a.__class__ = lambda: 0
# print(type(a))

a.__class__ = int
print(a)
print(type(a))

# __class__ on PyPy
a = {}
class C:
    def __new__(cls):
        return 0
a.__class__ = C
print(type(a))

# __class__.__class__ on CPython
# class C:
#     pass
# class
