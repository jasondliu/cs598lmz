from types import FunctionType
list(FunctionType(lambda:0,{}).__globals__.keys())

# ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__annotations__', '__builtins__', '__file__', '__cached__', '__builtin_module_names']

# 使用__globals__属性获取全局变量的字典，然后使用keys()方法获取所有的键值，最后使用list()函数转换为列表。

# 使用dir()函数
# 使用dir()函数可以获得一个对象所有的属性和方法，包括从父类继承的属
