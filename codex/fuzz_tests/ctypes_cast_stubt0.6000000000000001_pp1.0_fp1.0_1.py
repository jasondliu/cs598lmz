import ctypes
ctypes.cast(id(x), ctypes.py_object).value

#%%
# 利用模块 sys 中的 getrefcount() 函数，查看对象的引用计数。
import sys
print(sys.getrefcount(x))

#%%
# 调用 del 删除对象，使引用计数减一。
del x
print(sys.getrefcount(x))

#%%
# 创建对象，引用计数加一。
y = x
print(sys.getrefcount(y))

#%%
# 改变 y 的值，引用计数不变。
y = [1, 2, 3]
print(sys.getrefcount(y))

#%%
# 对象的引用
