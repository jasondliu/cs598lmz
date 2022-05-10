import weakref
# Test weakref.ref(int)
for i in range(1000):
    r = weakref.ref(i)
    assert r() is i


class A:
    pass

def foo():
    a = A()
    a.ref = weakref.ref(a)

foo()
for i in range(1000):
    foo()

import operator

def run(func, arg):
    for i in range(100000):
        func(arg)


class A:
    pass

a = A()

run(operator.setitem, (a, 'foo', 42))
run(operator.delitem, (a, 'foo'))

run(operator.setitem, ([], 42, 42))
run(operator.delitem, ([], 42))

run(operator.setitem, ({}, 1, 42))
run(operator.delitem, ({}, 1))

run(operator.setitem, (bytearray(b'abcdefg'), 42, 42))
run(operator.delitem, (bytearray(b'abcdefg'), 42))


