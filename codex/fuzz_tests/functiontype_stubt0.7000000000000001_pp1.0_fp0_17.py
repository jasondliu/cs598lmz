from types import FunctionType
a = (x for x in [1])
print(type(a))
def a(a):
    print(a)
    return a
print(type(a))
print(type(FunctionType))

print(type(isinstance))

# <class 'type'>
# <class 'type'>
# <class 'type'>
# <class 'type'>


class A:
    pass

class B(A):
    pass

print(type(A))
print(type(B))
# <class 'type'>
# <class 'type'>

print(A.__bases__)
# (<class 'object'>,)

print(B.__bases__)
# (<class '__main__.A'>,)

# type是元类，元类（metaclass）是用来创建类的类（基于元类的类创建出来的对象，就是类）
