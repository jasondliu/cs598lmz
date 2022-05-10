import types
# Test types.FunctionType
try:
    types.FunctionType
except AttributeError:
    pass
else:
    raise TestFailed, 'types.FunctionType should not exist'

# Test types.MethodType
try:
    types.MethodType
except AttributeError:
    pass
else:
    raise TestFailed, 'types.MethodType should not exist'

# Test types.BuiltinMethodType
try:
    types.BuiltinMethodType
except AttributeError:
    pass
else:
    raise TestFailed, 'types.BuiltinMethodType should not exist'

# Test types.ClassType
try:
    types.ClassType
except AttributeError:
    pass
else:
    raise TestFailed, 'types.ClassType should not exist'

# Test types.UnboundMethodType
try:
    types.UnboundMethodType
except AttributeError:
    pass
else:
    raise TestFailed, 'types.UnboundMethodType should not exist'

# Test types.InstanceType
try:
    types.InstanceType
except AttributeError:
    pass
