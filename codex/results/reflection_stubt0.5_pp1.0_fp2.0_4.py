fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #19353: Crash when using a non-callable as __code__
class NonCallable:
    def __call__(self):
        pass

def f():
    pass

f.__code__ = NonCallable()
f()
