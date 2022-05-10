fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn._defaults__ = (1, 2)
print(fn)
fn()
"""
"""
# Raw Exec
def f(x):
    def g(y):
        return x+y
    return g

c = compile("x = [1, 2, 3]\nf = lambda x: x+'s'\nprint(f(x))", "<string>", "exec")
exec(c)
print('x =', x)
print('f =', f)
"""
