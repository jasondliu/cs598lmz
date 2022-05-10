from types import FunctionType
a = (x for x in [1])
b = [1]
c = {1}
d = {1:1}
e = 1
f = b
g = FunctionType
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))

# isinstance(object, classinfo)
# 如果 object 是 classinfo 的实例，或者是一个 classinfo 子类的实例，则返回 True
print(isinstance(a, (int, list, tuple)))
print(isinstance(b, (int, list, tuple)))
print(isinstance(c, (int, list, tuple)))
print(isinstance(d, (int, list, tuple)))
print(isinstance(e, (int, list, tuple)))
print(isinstance(f, (int, list, tuple)))
print(isinstance(g, (int, list, tuple)))

