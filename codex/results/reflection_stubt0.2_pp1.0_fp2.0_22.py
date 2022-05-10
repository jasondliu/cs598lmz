fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test that the __code__ attribute can be set to a non-code object
# with a __call__ method.

class Callable:
    def __call__(self):
        return 42

fn.__code__ = Callable()
assert fn() == 42

# Test that the __code__ attribute can be set to a non-code object
# with a __call__ method that takes arguments.

class CallableWithArgs:
    def __call__(self, arg):
        return arg

fn.__code__ = CallableWithArgs()
assert fn(42) == 42

# Test that the __code__ attribute can be set to a non-code object
# with a __call__ method that takes keyword arguments.

class CallableWithKwargs:
    def __call__(self, arg=None):
        return arg

fn.__code__ = CallableWithKwargs()
assert fn(arg=42) == 42

# Test that the __code__ attribute can be set to a non-code object
# with a __call__ method
