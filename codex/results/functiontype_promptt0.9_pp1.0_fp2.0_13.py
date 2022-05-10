import types
# Test types.FunctionType()
try:
    types.FunctionType(1, 2, 3, 4)
except TypeError:
    pass
else:
    print('AssertionError')

# Test types.BuiltinFunctionType()
try:
    types.BuiltinFunctionType(1, 2, 3, 4)
except TypeError:
    pass
else:
    print('AssertionError')

# Test types.ModuleType()
try:
    types.ModuleType(1, 2, 3, 4)
except TypeError:
    pass
else:
    print('AssertionError')


## Issue #9342.
import types, sys
# Validate properties of built-in types such as bool.
try:
    sys.maxunicode > types.ModuleType.__mro__[0].__len__('')
except:
    print('Bug #9342')


## Issue #18975.
try:
    types.GetSetDescriptorType.__get__
except:
    pass
