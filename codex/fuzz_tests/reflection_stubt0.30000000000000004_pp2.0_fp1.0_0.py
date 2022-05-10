fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# test_generator_finalizer
def g():
    yield 1
    yield 2
g()

# test_generator_finalizer_raise
def g():
    try:
        yield 1
    finally:
        raise Exception
g()

# test_generator_finalizer_raise_2
def g():
    try:
        yield 1
    finally:
        yield 2
        raise Exception
g()

# test_generator_finalizer_raise_3
def g():
    try:
        yield 1
    finally:
        try:
            yield 2
        finally:
            raise Exception
g()

# test_generator_finalizer_raise_4
def g():
    try:
        yield 1
    finally:
        try:
            yield 2
        finally:
            yield 3
            raise Exception
g()

# test_generator_finalizer_raise_5
def g():
    try:
        yield 1
    finally:
        try:
            yield 2
        finally:
            try:

