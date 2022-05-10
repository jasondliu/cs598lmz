fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# test_generator_send_throw
def f():
    yield
f().throw(ValueError)

# test_generator_throw_stopiteration
def f():
    yield
f().throw(StopIteration)

# test_generator_throw_generatorexit
def f():
    yield
f().throw(GeneratorExit)

# test_generator_throw_generatorreturn
def f():
    yield
f().throw(GeneratorReturn)

# test_generator_throw_generatorreturn_value
def f():
    yield
f().throw(GeneratorReturn, 42)

# test_generator_throw_generatorreturn_value_after_yield
def f():
    yield 1
f().throw(GeneratorReturn, 42)

# test_generator_throw_generatorreturn_value_after_yield_value
def f():
    yield 1
    yield 2
f().throw(GeneratorReturn, 42)

# test_generator_throw_generatorreturn_value_after_y
