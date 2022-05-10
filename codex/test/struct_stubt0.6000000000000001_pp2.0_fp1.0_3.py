from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'i'
s.size = 4
s.pack

# In [21]:
# 这是一个文档字符串
def f():
    '''
    这是一个文档字符串
    '''

f.__doc__

# In [22]:
# 查看一个函数的属性
dir(f)

# In [23]:
# 查看一个函数的属性
dir(f.__code__)

# In [25]:
# 查看一个函数的属性
f.__code__.co_varnames

# In [26]:
# 查看一个函数的属性
f.__code__.co_argcount

# In [27]:
# 查看一个函数的
