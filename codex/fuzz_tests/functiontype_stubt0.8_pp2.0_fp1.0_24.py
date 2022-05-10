from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type((lambda x: x)))
print(type([]))
print(type({}))
print(type(None))
print(type(1))
print(type(1.2))
print(type('a'))
print(type(FunctionType))
print(type(1,))

# <class 'generator'>
# <class 'function'>
# <class 'list'>
# <class 'dict'>
# <class 'NoneType'>
# <class 'int'>
# <class 'float'>
# <class 'str'>
# <class 'type'>
# Traceback (most recent call last):
#   File "/Code/venv/chapter15/15.1.py", line <>, in <module>
#     print(type(1,))
# TypeError: type() takes 1 or 3 arguments


def foo():
    pass

class A():
    pass

print(type(foo))
print(type(A))
