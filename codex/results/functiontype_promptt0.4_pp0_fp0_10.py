import types
# Test types.FunctionType

def f(): pass

def g(): pass

def h(): pass

def test_function_type():
    assert types.FunctionType(f.func_code, f.func_globals, f.func_name,
                              f.func_defaults, f.func_closure) == f
    assert types.FunctionType(g.func_code, g.func_globals, g.func_name,
                              g.func_defaults, g.func_closure) == g
    assert types.FunctionType(h.func_code, h.func_globals, h.func_name,
                              h.func_defaults, h.func_closure) == h

def test_function_type_with_kwargs():
    # FunctionType can take keyword arguments as well
    f = types.FunctionType(code=f.func_code, globs=f.func_globals,
                           name=f.func_name, defaults=f.func_defaults,
                           closure=f.func_closure)
    assert f == f
