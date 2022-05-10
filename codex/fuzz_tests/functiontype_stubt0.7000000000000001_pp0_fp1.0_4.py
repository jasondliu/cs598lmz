from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type({}))
print(type([]))
print(type(()))
print(type(''))
print(type(6))
print(type(lambda x: x))
print(type(FunctionType(lambda x: x, {})))

"""
<class 'generator'>
<class 'dict'>
<class 'list'>
<class 'tuple'>
<class 'str'>
<class 'int'>
<class 'function'>
<class 'function'>
"""
