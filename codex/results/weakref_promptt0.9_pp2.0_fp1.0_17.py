import weakref
# Test weakref.ref(), where the target is a builtin class.
# Also see the implementation-specific part of test_weakref.
TestClass = type('TestClass', (object,), {})

class Foo(object):
    pass

r = weakref.ref(TestClass)
print()
print('Test 001: weakref.ref(TestClass)')
print(r())
r = weakref.ref(Foo)
print()
print('Test 002: weakref.ref(Foo)')
print(r())
print()
print('Test 003: r = weakref.ref(Foo()); print(r())')
r = weakref.ref(Foo())
print(r())
print()
# Test weakref.getweakrefcount() by calling it on a builtin class.
# Also see the implementation-specific part of test_weakref.
print('Test 004: getweakrefcount(TestClass)')
ret = weakref.getweakrefcount(TestClass)
print(ret)
print()
print('Test 005: getweakrefcount(Foo)')

