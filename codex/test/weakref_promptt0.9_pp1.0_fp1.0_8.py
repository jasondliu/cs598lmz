import weakref
# Test weakref.ref() and weakref.proxy() for callable objects.
import threading


class D(object):

    def work(self):
        return 111
    work = staticmethod(work)


d = D()


class C(object):

    def __init__(self, foo):
        self.foo = foo

    def __call__(self):
        return self.foo()
#        return self.foo


try:
    r = weakref.ref(d.work)
except TypeError:
    import sys
    print("SKIP")
    sys.exit()

if r() != 111:
    print("bad result from weak referent")

f = C(d.work)
if f() != 111:
    print("bad result from C instance")

p = weakref.proxy(f)
if p() != 111:
    print("bad result from weak proxy")


def ref_cb(r):
    print("weakref callback, %r dead" % (r, ))
weakref.add_callback(f, ref_cb)

t = thread
