import types
# Test types.FunctionType
def strange():
    pass
strange1 = types.FunctionType(strange.__code__, globals(), strange.__name__)
strange2 = types.FunctionType(strange.__code__, globals(), strange.__name__, strange.__defaults__)
print(strange1)
print(strange2)

# Test types.CodeType
def strange():
    pass
def test_code_type(fn):
    print(types.CodeType(fn.__code__.co_argcount, fn.__code__.co_kwonlyargcount, fn.__code__.co_nlocals, fn.__code__.co_stacksize, fn.__code__.co_flags, fn.__code__.co_code, fn.__code__.co_consts, fn.__code__.co_names, fn.__code__.co_varnames, fn.__code__.co_filename, fn.__code__.co_name, fn.__code__.co_firstlineno, fn.__code__.co_
