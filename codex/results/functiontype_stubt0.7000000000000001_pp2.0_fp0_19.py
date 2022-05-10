from types import FunctionType
a = (x for x in [1])
b = [1]
c = 1
print(type(a))
print(type(b))
print(type(c))
print(type(lambda x:x+3))
print(type(FunctionType))
print(type(isinstance))

# 查看类的继承关系
print(type(int).__bases__)
print(int.__bases__)
# 查看类方法
print(dir(int))
print(dir(list))

# 判断类型是否相同
print(type(int)==type(str)) # True
print(type(int)==type(int)) # True
print(type(str)==type(str)) # True
print(type(str)==type(int)) # False
print(type(int)==int) # False
print(type(str)==str) # False

print(type(int)==type(type(int))) # True
# 对
