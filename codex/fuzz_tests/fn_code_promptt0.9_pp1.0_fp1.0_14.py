fn = lambda: None
# Test fn.__code__.co_varnames in a function not declared using def or lambda
# or using exec.
# This creates a function using types.FunctionType.  Also test
# fn.__name__ and fn.__defaults__.
trace_fn = types.FunctionType(co, globals(), "trace_fn", (1, 2), None)

# Create a function with some annotations
def annotated_fn(larg, *args, **kwargs) -> 'just_a_string':
    print(6, args)
    print(7, kwargs)
    return larg

def simple_classmethod(cls): pass
simple_classmethod.__annotations__[0] = complex  # just to have something

def simple_staticmethod(): pass
simple_staticmethod.__annotations__[0] = complex  # just to have something

def bare_staticmethod(*args, **kwargs):
    pass

class Complex:
    classmethod_cm = classmethod(simple_classmethod)
    staticmethod_sm = staticmethod(simple_staticmethod)
    bare_staticmethod =
