fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# yields a generator iterator which when passed to __code__ must return a func
# object which when called will run the generated code

def f():
  yield 1

def g():
  yield f.__code__

def h():
  return g().next()()

h()

# calling a generator iterator which yields a code object which is called
# must run the generated code.

def f():
  return yield 1

def g():
  try:
    yield f().send(12)
  except TypeError:
    yield None

def h():
  return g().next()

h()

# yield 1 from f: calling a generator iterator which yields a value from a yield
# expression in a genexp

(yield 1 for i in ())

# yield 1 from () from a genexp

lambda: (yield 1 for i in ())

# yield 1 from () from a lambda

def f():
  return (yield 1 for i in ())

def g():
  return f()

def h():
  return g()
