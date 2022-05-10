fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# test_code_with_closure

def f():
    a = 1
    b = 2
    def g():
        return a + b
    return g

f.__code__.co_freevars
f.__closure__[0].cell_contents

# test_code_with_closure_and_dict

def f():
    a = 1
    b = 2
    def g():
        return a + b
    g.x = 42
    return g

f.__code__.co_freevars
f.__closure__[0].cell_contents
f().__closure__[0].cell_contents

# test_code_with_cellvars

def f():
    a = 1
    b = 2
    def g():
        a = 3
        return a + b
    return g

f.__code__.co_cellvars
f().__closure__[0].cell_contents

# test_code_with_cellvars_and_freevars

def
