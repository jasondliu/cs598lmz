fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# test_code_closure
def f():
    def g():
        return 1
    return g

f.__code__.co_freevars
f().__closure__[0].cell_contents

# test_code_closure_cell_contents
def f():
    x = 1
    def g():
        return x
    return g

f.__code__.co_freevars
f().__closure__[0].cell_contents

# test_code_closure_cell_contents_unbound
def f():
    x = 1
    def g():
        return x
    return g

f.__code__.co_freevars
f().__closure__[0].cell_contents

# test_code_closure_cell_contents_unbound_2
def f():
    x = 1
    def g():
        return x
    return g

f.__code__.co_freevars
f().__closure__[0].cell_contents

# test_code_closure
