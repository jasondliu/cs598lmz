fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #23398: Check that the exception raised by the generator
# expression is the same as the one raised by the generator function.
def gen():
    yield 1
    yield 2
    yield 3

def gen_exc():
    yield 1
    yield 2
    raise ValueError

def gen_exc2():
    yield 1
    yield 2
    raise StopIteration

def gen_exc3():
    yield 1
    yield 2
    raise StopAsyncIteration

def gen_exc4():
    yield 1
    yield 2
    raise RuntimeError

def gen_exc5():
    yield 1
    yield 2
    raise GeneratorExit

def gen_exc6():
    yield 1
    yield 2
    raise SystemExit

def gen_exc7():
    yield 1
    yield 2
    raise Exception

def gen_exc8():
    yield 1
    yield 2
    raise ArithmeticError

def gen_exc9():
    yield 1
    yield 2
    raise KeyError

def gen_exc10():
    yield 1
