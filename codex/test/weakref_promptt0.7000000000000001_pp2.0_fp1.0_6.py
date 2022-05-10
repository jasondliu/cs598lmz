import weakref
# Test weakref.ref:
class C:
    pass
o = C()
r = weakref.ref(o)
print(r)
print(r())
o2 = r()
print(o is o2)
# Test weakref.WeakKeyDictionary:
d = weakref.WeakKeyDictionary()
o = C()
d[o] = 1
print(d[o])
del o
print(d)

class MyList(list):
    pass

print(MyList.__mro__)
print(type(MyList))
print(type(list))

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

print(D.__mro__)
print(type(D))


class A:
    def foo(self):
        print('A')

class B(A):
    def foo(self):
        print('B')

class C(A):
    def foo(self):
        print('C')

