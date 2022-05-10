import select
# Test select.select()
#
# In [1]: import select
# In [2]: select.select([1, 2, 3], [], [], 0)
# Out[2]: ([1, 2, 3], [], [])
# In [3]: select.select([1, 2, 3], [], [], 1)
# Out[3]: ([1, 2, 3], [], [])
# In [4]: select.select([1, 2, 3], [], [], 5)
# Out[4]: ([1, 2, 3], [], [])
# In [5]: select.select([1, 2, 3], [], [], -1)
# Out[5]: ([1, 2, 3], [], [])
# In [6]: select.select([1, 2, 3], [], [], -5)
# Out[6]: ([1, 2, 3], [], [])
# In [7]: select.select([1, 2, 3], [], [], None)
# Out[7]: ([1, 2, 3], [], [])
# In [8]: select.
