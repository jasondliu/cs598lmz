import ctypes
ctypes.cast(id(x), ctypes.py_object).value

#%%
# 创建类
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x

obj = MyObject()

print(hasattr(obj, 'x')) # 有属性'x'吗？
print(obj.x)
print(hasattr(obj, 'y')) # 有属性'y'吗？
setattr(obj, 'y', 19) # 设置一个属性'y'
print(hasattr(obj, 'y')) # 有属性'y'吗？
print(getattr(obj, 'y')) # 获取属性'y'
print(obj.y) # 获取属性'y'

print(getattr(obj, 'z', 404
