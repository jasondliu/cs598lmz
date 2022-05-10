fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# test_generator_send_close
def gen():
    try:
        yield
    except GeneratorExit:
        print("closed")

g = gen()
next(g)
g.close()

# test_generator_throw
def gen():
    try:
        yield
    except ValueError:
        print("caught")

g = gen()
next(g)
g.throw(ValueError)

# test_generator_throw_stopiteration
def gen():
    try:
        yield
    except StopIteration:
        print("caught")

g = gen()
next(g)
g.throw(StopIteration)

# test_generator_throw_generatorexit
def gen():
    try:
        yield
    except GeneratorExit:
        print("caught")

g = gen()
next(g)
g.throw(GeneratorExit)

# test_generator_throw_other
def gen():
    try:
        yield
    except TypeError:
        print("
