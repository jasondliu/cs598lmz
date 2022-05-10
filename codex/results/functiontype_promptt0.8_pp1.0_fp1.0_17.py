import types
# Test types.FunctionType exists
import types
assert hasattr(types, 'FunctionType') and isinstance(types.FunctionType, type)

import sys
# Test type(lambda x: 3) == types.FunctionType
assert type(lambda x: 3) is types.FunctionType

# Test type(lambda x: 3) == types.LambdaType
assert type(lambda x: 3) is types.LambdaType
# Test hasattr(__builtins__, 'raw_input')
assert hasattr(__builti
