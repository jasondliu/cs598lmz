fn = lambda: None
# Test fn.__code__.co_filename:

# In [1]: fn.__code__.co_filename
# Out[1]: '&lt;ipython-input-4-e7b1b2d4f7a4&gt;'
# Test fn.__code__.co_firstlineno:

# In [2]: fn.__code__.co_firstlineno
# Out[2]: 4
# Now, I can create a function object with the same filename and first line number:

# In [3]: fn_ = types.FunctionType(fn.__code__, globals(), 'fn_', None, None)
# In [4]: fn_.__code__.co_filename
# Out[4]: '&lt;ipython-input-4-e7b1b2d4f7a4&gt;'
# In [5]: fn_.__code__.co_firstlineno
# Out[5]: 4
</code>

