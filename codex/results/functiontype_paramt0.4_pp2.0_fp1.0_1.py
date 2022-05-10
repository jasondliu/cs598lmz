from types import FunctionType
list(FunctionType(f.__code__, globals(), "my_function"))

# In[ ]:


# 使用types模块中定义的常量去测试对象的类型
import types
def fn():
    pass
type(fn)==types.FunctionType
type(abs)==types.BuiltinFunctionType
type(lambda x: x)==types.LambdaType
type((x for x in range(10)))==types.GeneratorType


# In[ ]:


# 使用isinstance()
# 对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数。
class Animal(object):
    pass
class Dog(Animal):
    pass
class Husky(Dog):
    pass
a = Animal()

