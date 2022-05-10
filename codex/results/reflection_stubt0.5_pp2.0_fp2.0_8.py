fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Should not raise a TypeError
fn.__code__ = gi.__iter__().__next__
fn()

# Should raise a TypeError
fn.__code__ = gi.__next__
fn()
"""

# test_code_new_kwonlyargcount

"""
def fn(a, *, b=1):
    pass

fn.__code__.co_kwonlyargcount
"""

# test_code_new_kwonlylocals

"""
def fn(a, *, b=1):
    pass

fn.__code__.co_kwonlylocals
"""

# test_code_new_posonlyargcount

"""
def fn(a, /, b=1):
    pass

fn.__code__.co_posonlyargcount
"""

# test_code_new_qualname

"""
def fn():
    pass

fn.__code__.co_qualname
"""

# test_code_new_stacksize

"""
def fn():
