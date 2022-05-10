fn = lambda: None
# Test fn.__code__.co_argcount
fn.__code__.co_argcount


# In[15]:


# Get function argcount/nargs (with no arg defaults) using argument unpacking
def get_fn_nargs_1(fn):
    return fn.__code__.co_argcount

get_fn_nargs_1(len)  # len() takes arbitary # args (like *args)


# In[16]:


# Annotating the fn definition but not call is allowed
def fn1(x: str, y: str) -> str:
    return x + y

fn1(2, 3)
# TypeError: Can't convert 'int' object to str implicitly


# In[17]:


# Test fn1.__annotations__
fn1.__annotations__   # dict, maps variablename to annotation


# In[18]:


# Passing 0 arguments and no defaults is OK for function call with annotated parameters
def fn1a(x: str, y: str):
    return x + y

fn1a()  # OK despite
