import ctypes
ctypes.cast(id(obj), ctypes.py_object).value

#%%
# 定义一个类，实现__len__方法
class MyLen(object):
    def __init__(self, num):
        self.num = num
    def __len__(self):
        return self.num

#%%
# 定义一个类，实现__getitem__方法
class MyGetItem(object):
    def __init__(self, num):
        self.num = num
    def __getitem__(self, index):
        if index >= self.num:
            raise IndexError
        else:
            return index

#%%
# 定义一个类，实现__setitem__方法
class MySetItem(object):
    def __init__(self, num):
        self.num = num
    def __setitem__(self, index, value):
        if index >= self.num
