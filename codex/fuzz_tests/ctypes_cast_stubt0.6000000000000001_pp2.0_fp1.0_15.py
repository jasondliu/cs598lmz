import ctypes
ctypes.cast(id(x), ctypes.py_object).value

#%%
# 计算一个字符串中每个字符出现的次数
s = 'asdfasdfasdfasdf'
d = {}
for c in s:
    d[c] = d.get(c, 0)+1

# 对于可变对象，直接作为键会有问题
d = {}
l = [1, 2, 3]
d[l] = 'a list'
l[0] = 0
d
# 解决方案
d = {}
d[tuple(l)] = 'a list'
d

#%%
# 对于不可变对象，可以直接使用setdefault替代get
d = {}
for c in s:
    d.
