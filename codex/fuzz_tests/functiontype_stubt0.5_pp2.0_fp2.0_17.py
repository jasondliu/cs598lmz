from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type([]))
print(type(list()))
print(type(str()))
print(type(FunctionType))
print(type(FunctionType()))
print(type(abs))
print(type(abs()))

print('\n\n')

# isinstance
print('isinstance:')
print(isinstance(a, (list, tuple)))
print(isinstance(a, (list, tuple, str)))
print(isinstance(a, (list, tuple, str, FunctionType)))
print(isinstance(a, (list, tuple, str, FunctionType, type)))
print(isinstance(a, (list, tuple, str, FunctionType, type, int)))
print(isinstance(a, (list, tuple, str, FunctionType, type, int, object)))
print(isinstance(a, (list, tuple, str, FunctionType, type, int, object, type)))
print(isinstance(a, (list, tuple, str, FunctionType, type, int, object, type, FunctionType)))
print(isinstance
