fn = lambda: None
# Test fn.__code__.co_varnames and fn.__code__.co_argcount
# and fn.__defaults__ and fn.__kwdefaults__
fn.__code__.co_varnames = (1, 2, 3)
fn.__code__.co_argcount = 4
fn.__defaults__ = (1, 2, 3)
fn.__kwdefaults__ = {'a': 1, 'b': 2}

# Test fn.__closure__
def make_closure(x):
    def closure():
        return x
    return closure

fn = make_closure(42)
fn.__closure__  # None or a tuple of cells

# Test fn.__annotations__
fn.__annotations__ = {'a': 1, 'b': 2}

# Test fn.__globals__
fn.__globals__ = {'a': 1, 'b': 2}

# Test fn.__dict__
fn.__dict__ = {'a': 1, 'b': 2}

# Test fn.__module__
fn.
