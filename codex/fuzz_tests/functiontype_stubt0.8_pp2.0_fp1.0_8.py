from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(gen_func))
print(type(gen_func()) == a)

"""
>>> type(a)
<class 'generator'>
>>> type(gen_func)
<class 'function'>
>>> type(gen_func()) == a
True
"""
