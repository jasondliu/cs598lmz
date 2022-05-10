fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'
fn.__doc__ = 'doc'
fn.__dict__ = {'a': 1}
fn.__defaults__ = (1, 2, 3)
fn.__globals__ = {'b': 2}
fn.__closure__ = (c for c in ())
fn.__annotations__ = {'c': 3}

print(fn.__code__)
print(fn.__name__)
print(fn.__doc__)
print(fn.__dict__)
print(fn.__defaults__)
print(fn.__globals__)
print(fn.__closure__)
print(fn.__annotations__)

# 函数的内省
# 函数的内省是指函数可以获取到自己的一些属性信息，比如函数名，函
