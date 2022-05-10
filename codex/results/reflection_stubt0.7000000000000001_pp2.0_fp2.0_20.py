fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()
 
# AttributeError: 'generator' object has no attribute 'co_code'
"""

"""
# Example 4: 

def fn():
    return
fn.__code__ = "not a code object"
fn()
 
# TypeError: __code__ must be set to a code object
"""

"""
# Example 5: 

def fn():
    return
fn.__code__ = fn.__code__.__class__.__new__(fn.__code__.__class__)
fn()
 
# ValueError: code object passed to ExecState.evalcode() is not valid
"""

"""
# Example 6: 

def fn():
    return
fn.__code__ = fn.__code__.__class__(
    fn.__code__.co_argcount,
    fn.__code__.co_kwonlyargcount,
    fn.__code__.co_nlocals,
    fn.__code__.co_stacksize,
    fn.__code__.co_flags,
