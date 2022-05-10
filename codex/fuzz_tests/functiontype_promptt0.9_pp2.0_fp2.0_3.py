import types
# Test types.FunctionType
# Deliberately put the module name at the start
assert types.MethodType.__module__ == types.__name__

# Test types.UnboundMethodtype
# Deliberately put the module name at the start
assert types.UnboundMethodType.__module__ == types.__name__

# Test types.StringType
# Deliberately put the module name at the start
assert types.StringType.__module__ == types.__name__

# Test types.IntType
# Deliberately put the module name at the start
assert types.IntType.__module__ == types.__name__

# Test types.FloatType
# Deliberately put the module name at the start
assert types.FloatType.__module__ == types.__name__

# Test types.LongType
# Deliberately put the module name at the start
assert types.LongType.__module__ == types.__name__

# Test types.TypeType
# Deliberately put the module name at the start
assert types.TypeType.__module__ == types.__name__

# Test types.Boo
