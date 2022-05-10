fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

# string in code.co_names
code = compile('a = 1', '', 'single')
names = code.co_names
names[1] = ''

# name in function.__globals__
class Cl(object):
    pass
def fn():
    pass
fn.__globals__['a'] = Cl()

# name in function.__closure__
def fn():
    pass
fn2 = lambda: None
fn2.__closure__ = (fn,)

# name in function.__defaults__
def fn(a=None):
    pass
fn.__defaults__ = (fn1,)

# name in function.__dict__
def fn():
    pass
fn.a = fn1

# name in class.__dict__
class Cl(object):
    pass
Cl.a = fn1

# name in instance.__dict__
class Cl(object):
    pass
inst = Cl()
inst.a = fn1

# name in method.__func__
class Cl(object):
    def fn(self
