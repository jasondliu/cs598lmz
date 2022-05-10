import types
# Test types.FunctionType
# Test to see if we can create and use a FunctionType instance

def f(x):
    return x*x

print 'f=', f
newfunc = types.FunctionType(f.func_code,f.func_globals,f.func_name,f.func_defaults,f.func_closure)
print 'newfunc=', newfunc
newfunc('def', 'ghi')
