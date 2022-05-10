import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
a = dict.fromkeys('abcdefghijklmnopqrstuvwxyz0123456789')
#print(gc.collect())
b = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5}
a.update(b)
#print(gc.collect())
del a['1']
#print(gc.collect())
del a
#print(gc.collect())


#print(gc.collect())

#print(gc.get_count())
# Inspecting the Garbage

# object_pairs_hook, optional function that will be called with the result of any dictionary conversion.
# The return value of object_pairs_hook will be used instead of the dict. This feature can be used to implement a custom dict
# objects. If object_pairs_hook is not given, the dict return.
def dict_maker(pairs):
    return {key: value for key, value in pairs}

# If object_pairs_hook is not given, the dict return.
print(json.loads('{"
