fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn()
f.__code__ = gi.gi_code
f()

# a generator function is a function
def f(): yield
print(f.__name__)

# a generator function is a function
def f(): yield
print(f.__code__)

# a generator function is a function
def f(): yield
print(f.__code__.co_code)

# a generator function is a function
def f(): yield
print(f.__code__.co_consts)

# a generator function is a function
def f(): yield
print(f.__code__.co_consts[0])

# a generator function is a function
def f(): yield
print(f.__code__.co_consts[0](1))

# a generator function is a function
def f(): yield
print(f.__code__.co_consts[0](1).send(None))

# a generator function is a function
def f(): yield
print(f.__code__.co_consts[0](1
