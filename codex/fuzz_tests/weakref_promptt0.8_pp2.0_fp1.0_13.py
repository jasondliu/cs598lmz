import weakref
# Test weakref.ref() call with an exception raised from __del__.
class A(object):

    def __del__(self):
        1 / 0
        return


try:
    ref = weakref.ref(A())
    ref()
except ZeroDivisionError:
    pass
else:
    raise Exception('unexpected success')
