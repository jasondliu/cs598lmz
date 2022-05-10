from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))
print(type(list))
print(isinstance(list, FunctionType))
print(type(lambda : ''))
print(type(type))

'''
<generator object <genexpr> at 0x7f907c7d1700>
<class 'generator'>
<class 'type'>
True
<class 'function'>
<class 'type'>
'''
