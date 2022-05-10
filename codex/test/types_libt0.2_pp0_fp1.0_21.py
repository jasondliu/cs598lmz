import types
types.MethodType(lambda self, x: x, None)

# In[ ]:

# 定义一个函数作为实例方法
def set_age(self, age):
    self.age = age

