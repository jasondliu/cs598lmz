import types
# Test types.FunctionType
f = types.FunctionType(types.CodeType(0, 0, 0, 0, '', (), (), (), '', '', 0, ''), types.ModuleType('foo'))
del f

# Test types.TypeType, TypeError
try:
    t = types.TypeType(1)
except TypeError:
    pass
else:
    raise "should have raised TypeError"
