import weakref
# Test weakref.ref(subclass instance)
#
# Some Python implementations seem to have an issue with weakrefs
# where the callable holds a reference to a class instance that
# happens to be a subclass of the target.  This test should
# help to show if a particular implementation exhibits this issue.

from weakref import ref


class A(object):

    def __init__(self, value):
        self.value = value


class B(A):
    pass


class C(A):

    def __init__(self, value):
        super(C, self).__init__(value)
        self.falue = value


def f(x):
    return x.value


a = A(1)
print(a.value)
r = ref(a, f)
print(r().value)

b = B(1)
print(b.value)
r = ref(b, f)
print(r().value)

c = C(1)
print(c.value)
r = ref(c, f)
print(r().value)
