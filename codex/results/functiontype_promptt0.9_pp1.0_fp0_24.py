import types
# Test types.FunctionType
def func(x):
    pass
func2 = lambda: None
func_str = str(func)
print types.FunctionType, func_str, 'is a %s' % type(func), type(func2)
setattr(types, 'FunctionType', func)
print types.FunctionType, func_str, 'is a %s' % type(func)
types.FunctionType = str
print types.FunctionType, func_str, 'is a %s' % type(func)
types.FunctionType = func
print types.FunctionType, func_str, 'is a %s' % type(func)
# Test types.BuiltinMethodType
blah = str.lower
blah2 = lambda x: x + ':boring'
blah_str = str(blah)
print types.BuiltinMethodType, blah_str, 'is a %s' % type(blah), type(blah2)
setattr(types, 'BuiltinMethodType', blah)
print types.BuiltinMethodType, blah_str, 'is a %s' % type(blah
