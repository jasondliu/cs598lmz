import weakref
# Test weakref.ref(). It doesn't work on default __main__.
# See test__main__.py.
x = []
x.append(weakref.ref(x))
print x[0]() is x

# Test weakref.proxy().
x = []
x.append(weakref.proxy(x))
print x[0] is x

# Test weakref.getweakrefcount().
print weakref.getweakrefcount([])
y = weakref.ref([])
print weakref.getweakrefcount([])
del y
print weakref.getweakrefcount([])

# Test getweakrefs().
x = []
print weakref.getweakrefs([]) == []
y = weakref.ref(x)
print weakref.getweakrefs(x) == [y]
del y
print weakref.getweakrefs(x) == []

# Test a weak reference to an instance method

# The test below triggers reference counting bug 929706:
# http://sourceforge.net/bugs/?func=detailbug&bug_id=929706&group
