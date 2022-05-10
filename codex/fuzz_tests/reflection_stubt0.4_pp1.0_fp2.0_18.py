fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# test_code_attributes
def f():
    pass
f.__code__ = 42

# test_code_attributes_2
def f():
    pass
f.__code__ = f

# test_code_attributes_3
def f():
    pass
f.__code__ = f.__code__

# test_code_attributes_4
def f():
    pass
f.__code__ = f.__code__.__code__

# test_code_attributes_5
def f():
    pass
f.__code__.__code__ = 42

# test_code_attributes_6
def f():
    pass
f.__code__.__code__ = f

# test_code_attributes_7
def f():
    pass
f.__code__.__code__ = f.__code__

# test_code_attributes_8
def f():
    pass
f.__code__.__code__ = f.__code__.__code__

# test
