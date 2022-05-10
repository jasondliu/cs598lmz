fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# test_generator_send_throw
def f():
    yield

g = f()
g.send(None)
g.throw(ValueError)

# test_generator_send_throw_return
def f():
    yield

g = f()
g.send(None)
g.throw(ValueError)
g.send(None)

# test_generator_send_throw_return_throw
def f():
    yield

g = f()
g.send(None)
g.throw(ValueError)
g.send(None)
g.throw(ValueError)

# test_generator_send_throw_return_throw_return
def f():
    yield

g = f()
g.send(None)
g.throw(ValueError)
g.send(None)
g.throw(ValueError)
g.send(None)

# test_generator_send_throw_return_throw_return_throw
def f():
    yield

g = f()
g.send(None
