from types import FunctionType
list(FunctionType('a','b','c'))

import types
mapping = [
    (types.FunctionType, lambda x: x.__name__),
    (str, lambda x: x.lower()),
    (list, lambda x: x[0]),
]
def dispatch(obj, mapping):
    for t, f in mapping:
        if isinstance(obj, t):
            return f(obj)
    return obj

print(dispatch(1,[]))
print(dispatch(lambda x: x**2, mapping))
print(dispatch('foo', mapping))
print(dispatch([1,2,3], mapping))

def dispatch(obj, mapping):
    for t, f in mapping:
        if isinstance(obj, t):
            return f(obj)
    return obj

dispatch(1,[])
dispatch(lambda x: x**2, mapping)
dispatch('foo', mapping)
dispatch([1,2,3], mapping)

def f(x):
    return x
dispatch(f, mapping)
dispatch(f, [(type
