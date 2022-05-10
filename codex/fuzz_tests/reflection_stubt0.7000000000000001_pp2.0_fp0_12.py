fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.__code__
fn()  # segfaults

# Work around in gdb:
# bt
# select-frame 0
# frame 2
# frame 1
# frame 2
# frame 1
# frame 2
# frame 1
# frame 2
# frame 1
# dis

def f():
    def g():
        for i in ():
            yield i
    return g

f()()
