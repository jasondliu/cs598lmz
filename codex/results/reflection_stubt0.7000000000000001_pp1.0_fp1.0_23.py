fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()


# In[ ]:


def f():
    raise StopIteration()

def g():
    yield f()

next(g())


# In[ ]:


fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()


# In[ ]:


def f():
    return lambda: None

def g():
    yield f()

g().send(None)()


# In[ ]:


fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()


# In[ ]:


def f():
    return None

def g():
    yield f()

g().send(None)()


# In[ ]:


fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()


# In[ ]:


def f():
    return __import__("sys").modules["os"]

def g():
    yield f()

g
