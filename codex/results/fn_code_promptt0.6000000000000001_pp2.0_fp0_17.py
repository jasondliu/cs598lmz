fn = lambda: None
# Test fn.__code__ can be set to None
try:
    fn.__code__ = None
except TypeError:
    pass
else:
    raise RuntimeError("fn.__code__ can be set to None")

# Test fn.__code__ can be set to a real code object
fn.__code__ = code
del code

# Test fn.__code__ can be set to a real function
fn.__code__ = fn

# Test fn.__code__ can be set to a builtin function
fn.__code__ = str

# Test fn.__code__ can be set to a builtin method
fn.__code__ = str.split

# Test fn.__code__ can be set to a method
fn.__code__ = TestClass.class_method

# Test fn.__code__ can be set to a static method
fn.__code__ = TestClass.static_method

# Test fn.__code__ can be set to a class method
fn.__code__ = TestClass.class_method

# Test fn.__code__ can be set to a function in a class
fn
