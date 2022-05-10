import weakref
# Test weakref.ref().
import support


class C(object):
    pass


def rc_helper(kwargs):
    return weakref.ref(C(), **kwargs)

rc = weakref.ref(C())
rp = weakref.proxy(C())
x = C()
s = weakref.finalize(x, lambda a: None)
del x

ref = weakref.ref(rc)
proxy = weakref.proxy(rp)

a = C()
b = C()

refs = [
    weakref.ref(a),
    weakref.ref(a),
    weakref.ref(a),
    weakref.ref(b)
]

del a
del b
res = list(filter(None, refs))
print(len(res) == 0)

if support.check_impl_detail():
    s = weakref.finalize(C()(), lambda a: None)
    unbound = weakref.finalize.__get__(None, C())
    unbound(C(), lambda a: None)
    wr =
