import types
types.NoneType
type(None)
type(5)
type([1,2,3])
type(lambda x: x)
type(None)
type(type)
type(lambda x: x)
type(lambda x: x) is types.LambdaType
type(lambda x: x) is types.FunctionType
type(lambda x: x) is types.GeneratorType
type(lambda x: x) is types.GeneratorType


# In[10]:


# https://www.bogotobogo.com/python/python_differences_between_static_method_and_class_method.php
class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'


# In[11]:


obj = MyClass()


# In[12]:


obj.method()


# In[13]:


obj.classmethod()


# In[
