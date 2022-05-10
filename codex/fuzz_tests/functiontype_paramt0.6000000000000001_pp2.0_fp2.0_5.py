from types import FunctionType
list(FunctionType(lambda: None, {}))
# Should work, but doesn't
list(FunctionType(lambda x: None, {}))
# Shouldn't work, but does
list(FunctionType(lambda x: None, {'x':None}))
# Shouldn't work, but does
list(FunctionType(lambda x: None, {'x':None}, None, None, None, None, None, None, None))
# Shouldn't work, but does
list(FunctionType(lambda x: None, {'x':None}, None, None, None, None, None, None, None, None))
# Shouldn't work, but does
list(FunctionType(lambda x: None, {'x':None}, None, None, None, None, None, None, None, None, None))
# Shouldn't work, but does
list(FunctionType(lambda x: None, {'x':None}, None, None, None, None, None, None, None, None, None, None))
# Shouldn't work, but does
list(FunctionType(lambda x: None, {'x':None}, None, None
