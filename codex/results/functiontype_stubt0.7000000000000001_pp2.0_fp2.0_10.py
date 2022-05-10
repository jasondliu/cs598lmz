from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a) is GeneratorType)
print(type(lambda: None) is GeneratorType)
print(type(a))
print(type(a) is FunctionType)
print(type(lambda: None) is FunctionType)

'''
<class 'generator'>
True
False
<class 'generator'>
False
True
'''

# 判断对象是否是可调用对象
print(callable(a))
print(callable(lambda: None))
print(callable((x for x in [1])))
print(callable([]))
print(callable('abc'))
print(callable(1))

'''
False
True
False
False
False
False
'''
