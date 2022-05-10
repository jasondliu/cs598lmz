fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test for issue #18084:
# https://bugs.python.org/issue18084
#
# A generator expression that yields from a generator should not
# be able to set its own __name__.
def gen():
    yield from (i for i in ())

gen.__name__ = 'foo'

# Test for issue #18085:
# https://bugs.python.org/issue18085
#
# A generator expression that yields from a generator should not
# be able to set its own __qualname__.
def gen():
    yield from (i for i in ())

gen.__qualname__ = 'foo'

# Test for issue #18086:
# https://bugs.python.org/issue18086
#
# A generator expression that yields from a generator should not
# be able to set its own __module__.
def gen():
    yield from (i for i in ())

gen.__module__ = 'foo'

# Test for issue #18087:
# https://bugs.python.org
