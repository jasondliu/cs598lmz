from types import FunctionType
a = (x for x in [1])
b = 1
print type(a)
print type(b)
print type(None)

print type(type(b))
print type([])
print type(str)
print type(int)
print type(dict)
print type(list)
print type(tuple)
print type(set)
print type(long)
print type(float)
print type(object)
print type(FunctionType)


# 判断class的类型，使用type()函数：

# >>> type(object)
# <type 'type'>

# 判断instance的类型，使用isinstance()函数：

# >>> class A(object):
#         pass
# >>> a = A()
# >>> isinstance(a, A)
# True
# >>> type(a) == A
# True
# >>> type(a) == type(A)
# False
# 通过type()函数判断的
