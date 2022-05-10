from types import FunctionType
list(FunctionType(code, globals(), 'module_2').__defaults__)

def module_3(a=None, b=None, c=None):
    pass
list(module_3.__defaults__)

def module_4(a=None, b=None):
    pass
list(module_4.__defaults__)

def module_5(a=None):
    pass
list(module_5.__defaults__)

def module_6(a=None):
    pass
list(module_6.__defaults__)


# In[43]:


def test(a,b,c,d,e,f):
    print(a,b,c,d,e,f)
test(1,2,3,4,5,6)


# In[ ]:


def test(a,b,c=3, d=4, e=5, f=6):
    print(a,b,c,d,e,f)
test(1,2)


# In[ ]:


def test(a,
