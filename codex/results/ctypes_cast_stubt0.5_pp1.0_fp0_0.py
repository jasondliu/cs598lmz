import ctypes
ctypes.cast(id(obj), ctypes.py_object).value

# 使用pickle模块
import pickle
pickle.dumps(obj)

# 使用copy模块
import copy
copy.copy(obj)
# 深拷贝
copy.deepcopy(obj)
'''

'''
# 使用__dict__属性

# 对象转字典
print(obj.__dict__)

# 模块转字典
import sys
print(sys.modules)

# 字典转对象
obj.__dict__ = {'a': 1, 'b': 2}
'''

'''
# 使用__slots__

class Student(object):
    __slots__ = ('name', 'age')

s = Student()
s.name = 'Michael'
s.age = 25

# s.score = 99

