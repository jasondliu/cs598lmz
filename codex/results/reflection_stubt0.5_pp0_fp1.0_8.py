fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()


# In[ ]:


def fn():
    print('hi')
fn.__code__ = 1
fn()


# In[ ]:


def fn():
    print('hi')
fn()
fn.__code__ = 1
fn()


# In[ ]:


fn.__code__ = None
fn()


# In[ ]:


def fn():
    print('hi')
fn.__code__ = None
fn()


# In[ ]:


def fn():
    print('hi')
fn.__code__ = object()
fn()


# In[ ]:


def fn():
    print('hi')
fn.__code__ = object
fn()


# In[ ]:


def fn():
    print('hi')
fn.__code__ = int
fn()


# In[ ]:


def fn():
    print('hi')
fn.__code__ = str
fn()


# In[ ]:


def fn():
    print('hi')
fn.__code__
