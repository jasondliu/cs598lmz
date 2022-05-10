fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# test_code_new_freevars
def f(x):
    def g(y):
        return x + y
    return g

f(1)(2)

# test_code_new_kwonlyargcount
def f(a, *, b):
    return a + b

f(1, b=2)

# test_code_new_posonlyargcount
def f(a, /, b):
    return a + b

f(1, 2)

# test_code_new_posonlyargcount_kwonlyargcount
def f(a, /, b, *, c):
    return a + b + c

f(1, 2, c=3)

# test_code_new_posonlyargcount_kwonlyargcount_annotations
def f(a: int, /, b: float, *, c: str):
    return a + b + len(c)

f(1, 2.0, c="foo")

# test_code_new_posonlyargcount
