gi = (i for i in ())
# Test gi.gi_code.co_flags

def f():
    yield 1
    yield 2

fgi = f()

for name in dir(fgi):
    attr = getattr(fgi, name)
    if hasattr(attr, '__call__'):
        try:
            attr()
        except TypeError:
            pass
        else:
            print('%s() did not raise TypeError' % name)

# Test gi.gi_frame.f_code.co_flags

def f():
    yield 1
    yield 2

fgi = f()
next(fgi)
fgi.gi_frame.f_code.co_flags
