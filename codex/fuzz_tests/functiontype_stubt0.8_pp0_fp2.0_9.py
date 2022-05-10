from types import FunctionType
a = (x for x in [1]) 
b = [1]
print(a)
print(b)
print(type(a))
print(type(b))
print(type([]))
print(type(()))
print(type(None))
print(type(lambda x: x+1))
print(FunctionType)
print(type(int))


# In[11]:


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
p1 = Point(1, 2)
print(p1.x)
# 是否能创建类型是Point的实例？
# 是否能创建类型是int型的实例？
# 是否能创建类型是FunctionType的实例？
print(isinstance(p1, Point))
print(isinstance(1, int))

