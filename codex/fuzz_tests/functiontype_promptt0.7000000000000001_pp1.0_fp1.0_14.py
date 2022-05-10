import types
# Test types.FunctionType:
def f(): pass
f_type = type(f)
assert isinstance(f, f_type)
assert isinstance(print, f_type)
assert isinstance(types.FunctionType.__init__, f_type)
assert isinstance(int, f_type)
assert not isinstance(1, f_type)
# Same for types.LambdaType
g = lambda: None
g_type = type(g)
assert isinstance(g, g_type)
assert isinstance(lambda: None, g_type)
assert not isinstance(1, g_type)
# Same for types.GeneratorType
h = (x for x in range(5))
h_type = type(h)
assert isinstance(h, h_type)
assert isinstance(x for x in range(5), h_type)
assert not isinstance(1, h_type)
