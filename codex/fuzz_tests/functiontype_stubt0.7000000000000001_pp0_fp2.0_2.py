from types import FunctionType
a = (x for x in [1])
b = [1,2,3]
c = {1:2}
d = FunctionType

print(isinstance(a,b))
print(isinstance(a,c))
print(isinstance(a,d))

print(isinstance(b,a))
print(isinstance(b,c))
print(isinstance(b,d))

print(isinstance(c,a))
print(isinstance(c,b))
print(isinstance(c,d))

print(isinstance(d,a))
print(isinstance(d,b))
print(isinstance(d,c))

# True
# True
# True
# True
# True
# False
# True
# True
# False
# True
# True
# True

# 一个对象可以同时属于多个类
# 对象可以与任何类进行比较，只要
