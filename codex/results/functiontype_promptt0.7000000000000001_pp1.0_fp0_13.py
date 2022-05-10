import types
# Test types.FunctionType is a function
assert(callable(types.FunctionType))

import json
# Test json.dumps is a function
assert(callable(json.dumps))

import sys
# Test sys.exit is a function
assert(callable(sys.exit))

# Test built-in print is a function
assert(callable(print))

# Test built-in str is a function
assert(callable(str))

# Test built-in type is a function
assert(callable(type))

# Test built-in range is a function
assert(callable(range))
