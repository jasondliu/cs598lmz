import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() max_n
n = gc.collect(1)
# Count objects before and after
n = gc.get_count()
print(n)
# s = set()
# for i in range(10):
#     s.add(weakref.ref(object()))
#     gc.collect(2)
#     assert len(s) >= n
# if we are tracking gc.DEBUG_COLLECTABLE then we need to temporarily
# disable it to allow objects to die that we created
n = gc.collect()
def func():
    # assert gc.collect() > 0
    # gc.collect(2)
    # for i in range(5):
    #     s.clear()
    #     for i in range(10):
    #         s.add(weakref.ref(object()))
    #     n = gc.collect(1)
    #     print(n)
    #     for ref in s:
    #         assert ref() is None # unresolved weakref
            # assert ref() is not None or n == 0 or i != 4
