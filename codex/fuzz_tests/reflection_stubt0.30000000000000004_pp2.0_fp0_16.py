fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #24071: Don't crash when a generator raises a StopIteration
# inside a finally block.
def f():
    try:
        yield
    finally:
        raise StopIteration

g = f()
next(g)
try:
    g.throw(StopIteration)
except StopIteration:
    pass

# Issue #24071: Don't crash when a generator raises a StopIteration
# inside a finally block.
def f():
    try:
        yield
    finally:
        raise StopIteration

g = f()
next(g)
try:
    g.close()
except StopIteration:
    pass

# Issue #24071: Don't crash when a generator raises a StopIteration
# inside a finally block.
def f():
    try:
        yield
    finally:
        raise StopIteration

g = f()
next(g)
try:
    g.send(None)
except StopIteration:
    pass

# Issue #24071: Don't crash when
