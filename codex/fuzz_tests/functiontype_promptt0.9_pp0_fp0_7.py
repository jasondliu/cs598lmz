import types
# Test types.FunctionType()

def test():
    return 1

print('types.FunctionType(): ', types.FunctionType(test.__code__, test.__globals__, name=test.__name__, argdefs=test.__defaults__, closure=test.__closure__))

# Test types.LambdaType()
# Only used internally by the interpreter

# Test types.CodeType()

def test():
    return 1

print('types.CodeType(): ', types.CodeType(test.__code__.co_argcount, test.__code__.co_kwonlyargcount, test.__code__.co_nlocals, test.__code__.co_stacksize, test.__code__.co_flags, test.__code__.co_code, test.__code__.co_consts, test.__code__.co_names, test.__code__.co_varnames, test.__code__.co_filename, test.__code__.co_name, test.__code__.co_firstlineno, test.__code
