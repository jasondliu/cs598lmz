fn = lambda: None
# Test fn.__code__
fn.__code__

# Test fn.__defaults__
txt = 'def fn(a=1, b=2):\n    return a'
exec(compile(txt, '', 'exec'), locals())
fn.__defaults__

# Test fn.__defaults__ attribute assignment
fn.__defaults__ = (3, 4)
fn()

# Test fn.__get__
class C:
    def f():
        pass

c = C()
c.f

# Test fn.__name__
fn.__name__


# Test types.FunctionType

# Test types.FunctionType()
types.FunctionType(fn.__code__, globals(), 'fn')

# Test types.FunctionType.__name__
types.FunctionType.__name__

# Test types.FunctionType.__doc__
types.FunctionType.__doc__


# Test types.MethodType

# Test types.MethodType()
c = C()
t = types.MethodType(fn, c)
t()

# Test types.MethodType
