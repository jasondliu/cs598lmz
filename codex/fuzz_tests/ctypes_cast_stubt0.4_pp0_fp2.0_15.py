import ctypes
ctypes.cast(id(obj), ctypes.py_object).value

# 更改对象的属性
obj.__dict__['name'] = 'new name'
obj.name

# 更改对象的方法
obj.__dict__['say'] = lambda self: 'new say'
obj.say()

# 新增对象的属性
obj.__dict__['new_attr'] = 'new attr'
obj.new_attr

# 新增对象的方法
obj.__dict__['new_method'] = lambda self: 'new method'
obj.new_method()

# 删除对象的属性
del obj.__dict__['name']
obj.name

# 删除对象的方法
del obj.__dict__['say']
obj.say()
