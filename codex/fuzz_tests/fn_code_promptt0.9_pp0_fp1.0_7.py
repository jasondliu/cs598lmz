fn = lambda: None
# Test fn.__code__
fn.__code__ = None
fn.__code__ = code
# Test fn.__defaults__
fn.__defaults__ = None
fn.__defaults__ = parameters
# Test fn.__globals__
fn.__globals__ = None
fn.__globals__ = globals
# Test fn.__kwdefaults__
fn.__kwdefaults__ = None
fn.__kwdefaults__ = None
fn.__kwdefaults__ = parameters
# Test fn.__name__
fn.__name__ = None
fn.__name__ = name

# Test fn2.__annotations__
fn2.__annotations__ = None
fn2.__annotations__ = parameters

# Test fn3.__closure__
fn3.__closure__ = None
fn3.__closure__ = globals
"""
        output = self.run_flake8(code, True)
        self.assertEqual(len(output), 0)
