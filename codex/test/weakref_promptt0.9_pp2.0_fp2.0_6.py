import weakref
# Test weakref.ref() and weakref.proxy()
class A:
    def __init__(self, value=10):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A()
w = weakref.ref(a)
p = weakref.proxy(a)
print(w())
# 10
print(p)
# 10

# Test WeakValueDictionary
d = weakref.WeakValueDictionary()
d['primary'] = a
print(d['primary'])
# 10
a = 1
