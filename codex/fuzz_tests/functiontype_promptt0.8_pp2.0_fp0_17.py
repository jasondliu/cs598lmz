import types
# Test types.FunctionType

# __main__
def f(): pass
assert type(f) == types.FunctionType

# __main__
class A:
    def f(): pass
assert type(A.f) == types.FunctionType

# __main__
class A:
    pass
a = A()
def f(): pass
a.f = f
assert type(a.f) == types.FunctionType

def test_pass_func_type(f):
    try:
        f(type(f))
    except TypeError:
        pass

# __main__
def f(): pass
test_pass_func_type(f)

# __main__
class A:
    def f(): pass
test_pass_func_type(A.f)

# __main__
class A:
    pass
a = A()
def f(): pass
a.f = f
test_pass_func_type(a.f)
