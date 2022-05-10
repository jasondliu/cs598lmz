fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn.__code__()

# https://github.com/python/cpython/blob/a0f7c8f6b1a8a8e6a3f3c3f9e9ddc8d5c67e7f2c/Objects/codeobject.c#L102-L107
def func(code, globals=None, name=None, argdefs=None, closure=None):
    """Create a function object from a code object and a dictionary.
    The optional name string overrides the name from the code object.
    The optional argdefs tuple specifies the default argument values.
    The optional closure tuple supplies the bindings for free variables.
    """
    return FunctionType(code, globals, name, argdefs, closure)

# https://github.com/python/cpython/blob/a0f7c8f6b1a8a8e6a3f3c3f9e9ddc8d5c67e7f2c/Objects/codeobject.c#L109-L114
def _make
