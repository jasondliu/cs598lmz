fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# issue #8
def f():
    def g():
        yield 1
    yield from g()

list(f())

# issue #9
def f():
    try:
        yield 1
    except:
        yield 2

list(f())

# issue #10
def f():
    try:
        yield 1
    finally:
        yield 2

list(f())

# issue #11
def f():
    try:
        yield 1
    except:
        yield 2
    finally:
        yield 3

list(f())

# issue #12
def f():
    try:
        yield 1
    except:
        yield 2
    else:
        yield 3

list(f())

# issue #13
def f():
    try:
        yield 1
    except:
        yield 2
    else:
        yield 3
    finally:
        yield 4

list(f())

# issue #14
def f():
    try:
        yield 1
    except:
        yield 2

