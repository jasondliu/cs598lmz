fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# test_code_attributes
def f(): pass
def g(): pass
f.__code__ = g.__code__

# test_code_co_filename
def f(): pass
f.__code__.co_filename = "spam"

# test_code_co_firstlineno
def f(): pass
f.__code__.co_firstlineno = 42

# test_code_co_flags
def f(): pass
f.__code__.co_flags = 42

# test_code_co_lnotab
def f(): pass
f.__code__.co_lnotab = "spam"

# test_code_co_name
def f(): pass
f.__code__.co_name = "spam"

# test_code_co_names
def f(): pass
f.__code__.co_names = ("spam",)

# test_code_co_nlocals
def f(): pass
f.__code__.co_nlocals = 42

# test_
