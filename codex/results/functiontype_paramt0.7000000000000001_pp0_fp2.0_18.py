from types import FunctionType
list(FunctionType(lambda:None,{}).__code__.co_varnames)

# In[6]:

def myfun(a,b):
    c = a + b
    return c

print(myfun(1,2))

# In[9]:

def myfun2(a,b):
    def c(x,y):
        return x + y
    return c(a,b)

print(myfun2(1,2))

# In[12]:

def myfun3(a,b):
    return a+b

print(myfun3(1,2))

# In[18]:

def func_h(x,y):
    return myfun3(x,y)

print(func_h(1,2))

# In[21]:

def func_h(x,y):
    return myfun3(x,y)

print(func_h(y=2,x=1))

# In[25]:

def func_h(*args,**kwargs):
    return
