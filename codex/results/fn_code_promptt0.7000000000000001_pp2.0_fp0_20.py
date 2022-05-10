fn = lambda: None
# Test fn.__code__ is a valid code object
fn.__code__ = 1
# Test fn.__defaults__ is a tuple
fn.__defaults__ = 'foo'
# Test fn.__globals__ is a dictionary (actually a mappingproxy)
fn.__globals__ = None
# Test fn.__closure__ is a tuple of cells
fn.__closure__ = (1, )
# Test fn.__annotations__ is a dictionary
fn.__annotations__ = 'foo'
# Test fn.__kwdefaults__ is a dictionary
fn.__kwdefaults__ = 'foo'
# Check the function is callable
fn()
# Check the function call raises an exception
fn()
# Check the function call raises an exception
fn()
# Check the function call raises an exception
fn()
# Check the function call raises an exception
fn()
# Check the function call raises an exception
fn()
# Check the function call raises an exception
fn()
