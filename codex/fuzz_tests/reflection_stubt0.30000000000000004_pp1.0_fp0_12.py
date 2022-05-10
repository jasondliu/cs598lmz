fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'
fn.__doc__ = 'doc'
fn.__module__ = 'module'
fn.__dict__ = {'key': 'value'}
fn.__defaults__ = (1, 2, 3)
fn.__closure__ = (1, 2, 3)
fn.__annotations__ = {'key': 'value'}
fn.__kwdefaults__ = {'key': 'value'}
print(fn)

# 查看函数的属性
print(fn.__code__)
print(fn.__code__.co_varnames)
print(fn.__code__.co_argcount)

# 查看函数的源码
print(fn.__code__.co_code)
print(fn.__code__.co_consts)
print(fn.__code__.co_names)
print(fn.__code__.co_varnames)
print(fn.__code
