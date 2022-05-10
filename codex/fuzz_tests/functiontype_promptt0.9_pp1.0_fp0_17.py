import types
# Test types.FunctionType and types.MethodType
for obj in [func, method, unbound]:
    assert isinstance(obj, types.FunctionType), repr(obj)
# Test new-style types.MethodType (static, class, unbound)
assert isinstance(static, types.MethodType)
assert isinstance(bound, types.MethodType)
assert isinstance(unbound, types.MethodType)
# Test a whole bunch of attrs are the same
for attr in ['__name__', '__doc__', '__dict__', '__globals__',
                    'func_name', 'func_doc', 'func_dict', 'func_code',
                    'func_defaults', 'func_globals', 'func_closure']:
   assert getattr(func, attr) == getattr(method, attr), repr(attr)
   assert getattr(func, attr) == getattr(unbound, attr), repr(attr)
   assert getattr(method, attr) == getattr(unbound, attr), repr(attr)
# Test args
assert func.func_
