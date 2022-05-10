import weakref
# Test weakref.ref


class C(object):
    def __del__(self):
        pass


r = weakref.ref(C())
r()
r.__call__()
r.__call__ is r()
# try:
#     r() is r().__call__
# except TypeError:
#     pass
# except AttributeError:
#     pass

# r().__call__()

# class ref_with_del(weakref.ref):
#     def ____del____(self):
#         pass


# try:
#     weakref.ref(C(), ref_with_del)
# except TypeError:
#     pass


class D(C):
    pass


# try:
#     weakref.proxy(D(), ref_with_del)
# except TypeError:
#     pass
