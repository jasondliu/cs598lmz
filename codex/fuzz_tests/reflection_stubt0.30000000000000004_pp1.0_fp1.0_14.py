fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# test_generator_send_after_throw
def gen():
    yield 1
    try:
        yield 2
    except ValueError:
        yield 3
    yield 4

g = gen()
assert next(g) == 1
assert next(g) == 2
try:
    g.throw(ValueError)
except ValueError:
    pass
assert next(g) == 4

# test_generator_throw_after_close
def gen():
    yield 1
    try:
        yield 2
    finally:
        yield 3
    yield 4

g = gen()
assert next(g) == 1
assert next(g) == 2
g.close()
assert next(g) == 3
try:
    next(g)
except StopIteration:
    pass

# test_generator_throw_after_close_in_except
def gen():
    try:
        yield 1
    except:
        yield 2
    yield 3

g = gen()
g.close()
assert next(g) == 2
try:
