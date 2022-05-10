fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# .pyo file
bf = (lambda c, a: c ^ a)
bt = (lambda c, a: c ^ a)
print(bf.__code__.co_code == bt.__code__.co_code)

# .pyo file
def bf(prog, *args):
    prog.__code__.co_code
    print(1)
def bt(prog, *args):
    prog.__code__.co_code
    print(1)
bf(bt)

# .pyc file
def f(x, y, z=3):
    """no comment"""
    return x + y + z

# .pyc file
def g():
    f(2, 3, 4)
