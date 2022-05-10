from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))
print(dir(a))
print(type(dir(a)))
print(type(dir(a)[0]))
print(type(dir(a)[0]) == FunctionType)

# 元组tuple
# 元组的元素不可变，但是元素的引用可变
t = (1, 2, 3)
print(t)
print(t[0])
print(t[0] == 1)
t[0] = 2
print(t[0])
print(t[0] == 1)

# 列表list
# 列表的元素可变
l = [1, 2, 3]
print(l)
print(l[0])
print(l[0] == 1)
l[0] = 2
print(l[0])
print(l[0] == 1)

# 字典dict
#
