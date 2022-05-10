import weakref
# Test weakref.ref(A())
# The weakref.ref(A()) will be a reference to the object A(),
# but since A() is not referenced anywhere else it will be
# destroyed at the end of the line.
# Test weakref.ref(A())
# The weakref.ref(a) will be a reference to the object a, a is
# referenced by a, but also by the weakref.ref(a), so it will
# not be destroyed.


class A(object):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str(self.value)


if __name__ == '__main__':
    a = A(10)
    d = weakref.WeakValueDictionary()
    d['primary'] = a
