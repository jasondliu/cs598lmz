import weakref
# Test weakref.ref(x) == weakref.ref(x)
# Test weakref.ref(x) is weakref.ref(x)
# Test x is weakref.ref(x)()
# Test x is weakref.ref(x).__call__()
# Test weakref.ref(x)(), weakref.proxy(x)()
# Test weakref.getweakrefcount()
# Test weakref.getweakrefs()
# Test weakref.getweakrefs(x)


class C:
    pass


def check(x, y):
    # Check weakref.ref(x) == weakref.ref(y)
    if x is y:
        print('x is y')
    else:
        print('x is not y')
    if weakref.ref(x) == weakref.ref(y):
        print('ref(x) == ref(y)')
    else:
        print('ref(x) != ref(y)')
