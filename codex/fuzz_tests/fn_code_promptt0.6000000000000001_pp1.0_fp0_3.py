fn = lambda: None
# Test fn.__code__.co_argcount
fn.__code__.co_argcount


# ## Functional Programming tools

# ### map

# In[21]:


# map(function, iterable, ...)
# Return an iterator that applies function to every item of iterable, yielding the results.
# If additional iterable arguments are passed, function must take that many arguments and is applied to the items from all iterables in parallel.
# With multiple iterables, the iterator stops when the shortest iterable is exhausted.
# For cases where the function inputs are already arranged into argument tuples, see itertools.starmap().

# map(function, iterable, ...)
# Return an iterator that applies function to every item of iterable, yielding the results.
# If additional iterable arguments are passed, function must take that many arguments and is applied to the items from all iterables in parallel.
# With multiple iterables, the iterator stops when the shortest iterable is exhausted.
# For cases where the function inputs are already arranged into argument tuples, see itertools.starmap().


# In[22]:


# example 1
def
