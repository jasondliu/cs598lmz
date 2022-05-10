import types
# Test types.FunctionType

# This, not
# def foo():
#     pass
# foo = types.FunctionType(foo.func_code, foo.func_globals, foo.func_name, foo.func_defaults, foo.func_closure)
# 
# but this.

def foo():
    pass

foo = types.FunctionType(foo.__code__, foo.__globals__, foo.__name__, foo.__defaults__, foo.__closure__)
