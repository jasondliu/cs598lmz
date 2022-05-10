from types import FunctionType
a = (x for x in [1])
print(type(a))

# 函数类型
print(type(abs))
print(type(lambda x:x+1))
print(type((x for x in [1])))
print(type(FunctionType))

print(isinstance(a,FunctionType))


# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
print(dir(a))

# 类似__xxx__的属性和方法在Python中都是有特殊用途的，比如
