fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.__code__
fn()


# In[64]:


#Function with a generator instead of the code object
def fn():
    for i in range(10):
        print(i)


# In[74]:


#function with generator as code object
fn.__code__ = (i for i in range(10)).__code__
fn()


# In[70]:


#Function with a Function instead of the code object
def fn():
    fn()


# In[72]:


fn.__code__ = fn
fn()


# # https://youtu.be/wfbJNrZdqVc
