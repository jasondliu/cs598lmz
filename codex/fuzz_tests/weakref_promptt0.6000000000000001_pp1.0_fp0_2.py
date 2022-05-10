import weakref
# Test weakref.ref()

class A:
    pass

a = A()
b = weakref.ref(a)
print(b())
print(a is b())
print(b() is None)
print(b().x)

a.x = 10
print(b() is None)
print(b().x)

a = None
print(b() is None)

del a
print(b() is None)

del b

# Test weakref.ref(x, callback)

# global gc_count
# gc_count = 0
# def gc_callback(obj):
#     global gc_count
#     print('gc_callback')
#     gc_count += 1
#
# a = A()
# b = weakref.ref(a, gc_callback)
# print('gc_count:', gc_count)
#
# a = None
# import gc
# gc.collect()
# print('gc_count:', gc_count)
#
# del b

# Test weakref.WeakValueD
