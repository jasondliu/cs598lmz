from types import FunctionType
list(FunctionType(teardown_function.func_code,globals(), 'teardown_function'))

teardown_function = FunctionType(teardown_function.func_code, globals(), 'teardown_function')

print teardown_function.__call__()

#print list(FunctionType(setup_function.func_code,globals(), 'setup_function'))
