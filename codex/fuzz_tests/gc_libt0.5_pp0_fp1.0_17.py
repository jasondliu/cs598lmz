import gc, weakref

# def f():
#     return 42
#
# def g():
#     return weakref.ref(f)
#
# r = g()
# print(r)
# print(r())
# del f
# print(r())

# class C:
#     def __init__(self, x):
#         self.x = x
#     def __repr__(self):
#         return 'C({})'.format(self.x)
#
# c = C(42)
# r = weakref.ref(c)
# print(r())
# print(r() is c)
# print(r() == c)
# del c
# print(r())
# print(gc.collect())
# print(r())

# class C:
#     def __init__(self, x):
#         self.x = x
#     def __repr__(self):
#         return 'C({})'.format(self.x)
#
# c = C(42)
# r = weakref.ref(c)
#
