import weakref
# Test weakref.ref

class A:
    def __init__(self):
        self.a = 1
    def __call__(self):
        print("A")

a = A()

# Create weak reference to a
r = weakref.ref(a)

print(r())
print(r()())

# Delete a
del a

print(r())

# Create another reference to a
a = A()

# Create another weak reference to a
r2 = weakref.ref(a)

print(r2())

# Delete a
del a

print(r2())

# Test weakref.WeakValueDictionary

class A:
    def __init__(self, num):
        self.num = num

a = A(1)
b = A(2)
c = A(3)

d = weakref.WeakValueDictionary()
d["a"] = a
d["b"] = b
d["c"] = c

print(d["a"].num)
print(d["b"].num)
