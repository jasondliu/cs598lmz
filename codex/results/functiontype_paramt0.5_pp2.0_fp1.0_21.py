from types import FunctionType
list(FunctionType(lambda: 1, {}))

# Confirm that we can still use the function after converting to a list.
FunctionType(lambda: 1, {})()

# Confirm that we can still use the function after converting to a list.
FunctionType(lambda: 1, {}).__call__()
