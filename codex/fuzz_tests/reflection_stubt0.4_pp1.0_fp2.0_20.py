fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()


# In[ ]:


def fn():
    yield 1
fn.__code__ = None
fn()


# In[ ]:


def fn():
    yield 1
fn.__code__ = 'a'
fn()


# In[ ]:


def fn():
    yield 1
fn.__code__ = 1
fn()


# In[ ]:


def fn():
    yield 1
fn.__code__ = (1, 2, 3)
fn()


# In[ ]:


def fn():
    yield 1
fn.__code__ = {1: 2}
fn()


# In[ ]:


def fn():
    yield 1
fn.__code__ = [1, 2, 3]
fn()


# In[ ]:


def fn():
    yield 1
fn.__code__ = {1, 2, 3}
fn()


# In[ ]:


def fn():
    yield 1
fn.__code__ = (i for i in ())
fn()


# In[
