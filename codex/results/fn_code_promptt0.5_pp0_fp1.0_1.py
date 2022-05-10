fn = lambda: None
# Test fn.__code__
try:
    fn.__code__
except AttributeError:
    print('SKIP')
    raise SystemExit

# Test fn.__defaults__
fn.__defaults__ = (1,)
print(fn.__defaults__)

# Test fn.__closure__
def outer():
    x = 1
    def inner():
        return x
    return inner

fn = outer()
print(fn.__closure__)
print(fn.__closure__[0].cell_contents)

# Test fn.__globals__
print(fn.__globals__)

# Test fn.__annotations__
def fn(a: 1):
    pass
print(fn.__annotations__)

# Test fn.__kwdefaults__
def fn(x, y=1):
    pass
print(fn.__kwdefaults__)
