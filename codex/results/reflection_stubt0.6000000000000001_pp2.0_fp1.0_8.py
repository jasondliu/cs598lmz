fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

s = pickle.dumps(fn)
load_global = pickle.loads(s)
print(load_global)

# The same thing, but with a class, and check the __dict__ too
class Foo:
    pass

f = Foo()
f.__code__ = gi
f.__dict__['foo'] = 'bar'
s = pickle.dumps(f)
load_class = pickle.loads(s)
print(load_class)
print(load_class.__dict__)

# Test the same thing with a function created with types.FunctionType
def f(x):
    return x

fn = types.FunctionType(f.__code__, f.__globals__, 'fn', (), ('x',))
fn.__code__ = gi
s = pickle.dumps(fn)
load_global = pickle.loads(s)
print(load_global)

# The same thing, but with a class created with types.FunctionType
class Foo:
    pass

f = Foo()

