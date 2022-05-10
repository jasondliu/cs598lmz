import types
# Test types.FunctionType and types.LambdaType
print('types.FunctionType: ', issubclass(types.FunctionType, object))
print('types.LambdaType: ', issubclass(types.LambdaType, object))
# Test function attributes.
print('Function.__name__: ', types.FunctionType.__name__)
print('Function.__module__: ', types.FunctionType.__module__)
print('Function.__dict__: ', types.FunctionType.__dict__)
print('Function.__doc__: ', types.FunctionType.__doc__)
print('Function.__text_signature__: ', types.FunctionType.__text_signature__)
print('Function.__qualname__: ', types.FunctionType.__qualname__)

# Test function behaviors.
def func(*args): return args
print('Function.__call__: ', types.FunctionType(func)(1, 2, 3))
# Test function behaviors.
def func2(self, *args): return args
print('Function.__call__: ', types.FunctionType(func2, 123)(
