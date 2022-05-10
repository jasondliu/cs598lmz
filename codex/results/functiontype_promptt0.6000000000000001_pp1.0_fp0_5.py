import types
# Test types.FunctionType to see if callback is a 'function'
if type(callback) == types.FunctionType:
    callback()

# Output:
# Callback function called

# Using the isinstance() function
import types
if isinstance(callback, types.FunctionType):
    callback()

# Output:
# Callback function called
