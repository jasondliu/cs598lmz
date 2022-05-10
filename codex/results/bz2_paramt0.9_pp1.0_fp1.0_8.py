from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(d)

# ## Profiling and benchmarking

# #### How long it takes to run a code

# In[27]:

# time it
import timeit
timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)


# In[28]:

timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)


# In[29]:

timeit.timeit('"-".join(map(str, range(100)))', number=10000)


# #### Profiling

# In[30]:

get_ipython().run_cell_magic('prun', '# this makes it line profiler', 'def sum_of_lists(N):\n    total = 0\n    for i in range(5):\n        L = [j ^ (j >> i) for j in range(N)]\n        total += sum(L)\n    return total\nsum_of_lists(100000)')


# In[31
