import weakref
# Test weakref.ref
class C:
    pass
o = C()
r = weakref.ref(o)
assert r() is o
del o
assert r() is None
assert r() is None
# Test weakref.proxy
p = weakref.proxy(o)
assert p is None

# WindowsError is raised directly on Windows
try:
    e = WindowsError()
except NameError:
    pass
else:
    if e.args[0] == 0: # XXX should not test the errno
        raise Exception("expected WindowsError to have a meaningful errno")

# WindowsError is raised directly on Windows
try:
    e = WindowsError(1)
except NameError:
    pass
else:
    if e.args[0] != 1:
        raise Exception("expected WindowsError to have an errno of 1")

# WindowsError is raised directly on Windows
try:
    e = WindowsError(1, "hello")
except NameError:
    pass
else:
    if e.args[0] != 1:
        raise Exception("expected WindowsError to have an errno of 1
