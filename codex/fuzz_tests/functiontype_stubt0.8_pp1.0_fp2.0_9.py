from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])

print(a)
print(id(a))
print(id(b))

print(a == b)

c = (x for x in [1])

print(isinstance(c, GeneratorType))
print(isinstance(c, types.GeneratorType))
print(type(c))
print(type((x for x in [1])))

print(FunctionType)
print(FunctionType == types.FunctionType)
print(isinstance(c, FunctionType))
print(isinstance(c, FunctionType))

print(types.TracebackType)
print(isinstance(c, types.TracebackType))

# 判断自定义类型
# print(types.ClassType)

# 类的判断推荐使用isinstance
print(isinstance(c, FunctionType))

# 判断类型的姿势
print(isinstance(c, (list
