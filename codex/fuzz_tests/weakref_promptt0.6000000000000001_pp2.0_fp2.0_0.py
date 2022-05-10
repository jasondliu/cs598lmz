import weakref
# Test weakref.ref()
import weakref
class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)
a = A(10)
r = weakref.ref(a)
print(r)
print(r())
a = A(20)
print(r())
print(r() is None)
print(r() is None)
class C:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)
c = C(10)
r = weakref.ref(c)
print(r)
print(r())
c = C(20)
print(r())
print(r() is None)
print(r() is None)
class G:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)
g = G(10)
r = weakref.ref(g)
