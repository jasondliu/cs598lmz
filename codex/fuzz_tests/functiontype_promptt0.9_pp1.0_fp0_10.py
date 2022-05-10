import types
# Test types.FunctionType type.

def f1(a):
    '''function created by def statement'''
    return a

def f2():
    return f1

def f3(a=None):
    '''function created by lambda statement'''
    return lambda b: a + b

def f4():
    return f3

def f5():
    return lambda a: f1(a)

def f6():
    return lambda a: f1(a)()

properties = dir(types.FunctionType)
assert 'func_closure' in properties
assert 'func_code' in properties
assert 'func_defaults' in properties
assert 'func_dict' in properties
assert 'func_globals' in properties
assert 'func_name' in properties

methods = dir(types.FunctionType.__doc__)
assert 'find' in methods
assert 'lower' in methods
assert 'replace' in methods
assert 'split' in methods

assert f2()(15) == 15
assert f4()()(15)(2) == 15 + 2
assert f5()
