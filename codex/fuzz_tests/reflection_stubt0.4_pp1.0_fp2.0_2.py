fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# test_generator_send_exception
def fn():
    try:
        yield 1
    except Exception:
        yield 2
    else:
        yield 3

g = fn()
g.send(None)
g.throw(Exception)
g.send(None)

# test_generator_throw_return
def fn():
    try:
        yield 1
    except Exception:
        yield 2
    else:
        yield 3

g = fn()
g.send(None)
g.throw(Exception)
g.send(None)
g.send(None)

# test_generator_throw_stopiteration
def fn():
    try:
        yield 1
    except Exception:
        yield 2
    else:
        yield 3

g = fn()
g.send(None)
g.throw(StopIteration)
g.send(None)

# test_generator_throw_generatorexit
def fn():
    try:
        yield 1
    except Exception:
        yield 2
   
