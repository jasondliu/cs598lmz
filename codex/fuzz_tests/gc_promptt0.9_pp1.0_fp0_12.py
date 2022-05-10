import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
a = []

print('Stack ref:', len(gc.get_referrers(a)))
del a
print('Heap ref: ', len(gc.get_referrers(gc.garbage[0])))

# Once unreachable, the memory may be erased.
# 
# Garbage collection occurs *at least* when the count reaches zero.
# 
# There is no guarantee when the memory will actually be freed.
# 
# Addendum
# 
# ```
# del x
# ```
# 
# is different from
# 
# ```
# x = None
# ```
# 
# The former actually deletes the variable, but the latter does not.
# 
# Consequently, the former makes the variable unreachable by any other variable (no other variable can refer it), but the latter does not.
