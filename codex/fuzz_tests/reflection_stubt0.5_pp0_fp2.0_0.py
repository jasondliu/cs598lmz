fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# test_nested_generator_expression
def fn():
    yield (i for i in range(10))

t = fn()
for i in t:
    assert next(i) == 0

# test_generator_expression_yield_from
def fn():
    yield from (i for i in range(10))

t = fn()
for i in t:
    assert i == 0

# test_generator_expression_yield_from_new_syntax
def fn():
    yield from (i for i in range(10))

t = fn()
for i in t:
    assert i == 0

# test_generator_expression_yield_from_new_syntax_2
def fn():
    yield from (i for i in range(10))

t = fn()
for i in t:
    assert i == 0

# test_generator_expression_yield_from_new_syntax_3
def fn():
    yield from (i for i in range(10))

t =
