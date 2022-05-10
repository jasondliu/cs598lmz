from types import FunctionType
a = (x for x in [1])
b = [x+1 for x in (1,2,3)]
print(a,b)
print(type(a), type(b))

d = 0
print(type(d))
c = True
print(type(c))

print(type(print))

print(isinstance([], list))
print(isinstance([], dict))
print(isinstance(print, FunctionType))

# callable 是否可以调用
print(callable(print))
print(callable(lambda x:x))

a = 123456
b = str(a)
print(b)
print(type(b))

x = "abcdee"
print(" ".join(x))

# 连接
a = ["a", "b", "c", "d"]
print("-".join(a))

# 转换成元组
b = tuple(a)
print(type(b))

a = "hello"
b = "world"
c =
