fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# With a generator that raises an exception
def g():
    yield 1
    raise StopIteration(2)

def fn():
    return (i for i in g())

try:
    fn()
except StopIteration as e:
    print(e.args[0])

# With a generator that returns a value
def g():
    yield 1
    return 2

def fn():
    return (i for i in g())

try:
    fn()
except StopIteration as e:
    print(e.args[0])

# With a generator that yields a value and then raises an exception
def g():
    yield 1
    raise StopIteration(2)
    yield 3

def fn():
    return (i for i in g())

try:
    fn()
except StopIteration as e:
    print(e.args[0])

# With a generator that yields a value and then returns a value
def g():
    yield 1
    return 2
    yield 3

def fn():
    return (i for
