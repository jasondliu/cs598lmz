fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #25879: Ensure that the __code__ attribute of a function is
# writeable.
import types
def f(): pass
f.__code__ = types.FunctionType(f.__code__.co_code, f.__code__.co_globals,
                                f.__code__.co_name, f.__code__.co_defaults,
                                f.__code__.co_closure)

# Issue #25886: Ensure that the __code__ attribute of a function is
# writeable.
def f(): pass
f.__code__ = f.__code__.__class__(f.__code__.co_code, f.__code__.co_globals,
                                  f.__code__.co_name, f.__code__.co_defaults,
                                  f.__code__.co_closure)

# Issue #25892: Ensure that the __code__ attribute of a function is
# writeable.
def f(): pass
f.__code__ = type(f.__
