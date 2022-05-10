import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

# class A(object):
#     pass
# a = A()
# id(a)
# del a
# a = A()
# id(a)

# gc.collect()
# class A(object):
#     pass

# a = A()
# b = A()
# a.b = b
# b.a = a
# id(a), id(b)
# del a
# gc.collect()
# id(b)
# del b
# gc.collect()
# class A(object):
#     def __del__(self):
#         print('A.__del__')

# a = A()
# b = A()
# a.b = b
# b.a = a
# id(a), id(b)
# del b
# gc.collect()
# del a
# gc.collect()
# class A(object):
#     def __del__(self):
#         print('A.__del__')

# a = A()
# b = A()
#
