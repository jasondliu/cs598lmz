from types import FunctionType
a = (x for x in [1])
b = [x for x in [2]]
print(type(a))
print(type(b))
print(type(print)) # <class 'builtin_function_or_method'>
print(type(lambda x:x)) # <class 'function'>
print(type((x for x in [3]))) # <class 'generator'>
print(type(abs)) # <class 'builtin_function_or_method'>
print(type(int)) # <class 'type'>
print(type(dict)) # <class 'type'>
print(type(a)) # <class 'generator'>
