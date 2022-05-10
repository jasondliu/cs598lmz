fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
try:
    exec(fn)
except TypeError:
    print('SKIP')
    raise SystemExit

# Verify that exec() works with a generator that has a __code__ attribute,
# but not a __next__ attribute.

class G:
    def __init__(self):
        self.i = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.i:
            raise StopIteration
        self.i += 1
        return 'print("hello")'

g = G()
g.__code__ = g
exec(g)
