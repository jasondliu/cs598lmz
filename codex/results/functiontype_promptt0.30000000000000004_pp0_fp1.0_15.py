import types
# Test types.FunctionType

def f(): pass

assert isinstance(f, types.FunctionType)
assert issubclass(types.FunctionType, object)
assert not issubclass(types.FunctionType, type)

assert types.FunctionType.__module__ == 'types'
assert types.FunctionType.__name__ == 'function'
assert types.FunctionType.__qualname__ == 'function'

assert types.FunctionType.__doc__ == 'function(code, globals[, name[, argdefs[, closure]]])\n\nCreate a function object from a code object and a dictionary.\nThe optional name string overrides the name from the code object.\nThe optional argdefs tuple specifies the default argument values.\nThe optional closure tuple supplies the bindings for free variables.\n'

assert types.FunctionType.__annotations__ == {}

assert types.FunctionType.__dict__ == {
    '__annotations__': {},
    '__call__': <slot wrapper '__call__' of 'function' objects>,
    '__class__': <class 'type'>,

