import ctypes
ctypes.cast(0, ctypes.py_object).value

# In[ ]:


# 创建一个类
class Student(object):
    pass

# 创建实例
bart = Student()
print(bart)
print(Student)

# In[ ]:


# 给实例绑定属性
bart.name = 'Bart Simpson'
print(bart.name)

# In[ ]:


# 给实例绑定方法
def set_age(self, age):
    self.age = age
from types import MethodType
bart.set_age = MethodType(set_age, bart)
bart.set_age(25)
print(bart.age)

# In[ ]:


# 给类绑定方法
def set_score(self, score):
    self.score = score
Student.set_score = set_score
bart.set_score(100
