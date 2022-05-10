import types
types.MethodType(lambda self: None, None)

# This should not crash
import types
types.MethodType(lambda self: None, None, None)

# This should not crash
import types
types.MethodType(lambda self: None, None, None, None)

# This should not crash
import types
types.MethodType(lambda self: None, None, None, None, None)

# This should not crash
import types
types.MethodType(lambda self: None, None, None, None, None, None)

# This should not crash
import types
