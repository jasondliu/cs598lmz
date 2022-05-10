fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #20897: test the __code__ attribute of a frame
def f():
    return sys._getframe()

frame = f()
code = frame.f_code

# Issue #20897: test the __code__ attribute of a traceback
try:
    1/0
except ZeroDivisionError:
    tb = sys.exc_info()[2]
    code = tb.tb_frame.f_code

# Issue #20897: test the __code__ attribute of a generator
def g():
    yield

gen = g()
code = gen.gi_code

# Issue #20897: test the __code__ attribute of a generator
def g():
    yield
    yield

gen = g()
next(gen)
code = gen.gi_code

# Issue #20897: test the __code__ attribute of a generator
def g():
    yield
    yield
    yield

gen = g()
next(gen)
next(gen)
code = gen.gi_code


