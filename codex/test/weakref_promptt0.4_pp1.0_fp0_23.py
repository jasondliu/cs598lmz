import weakref
# Test weakref.ref()

# Create a weak reference to an object

class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)               # create a reference
d = weakref.ref(a)
print(d)                # print the reference
print(d())              # print the object
print(d() is a)         # verify that the reference is to the original object

# Create a weak reference to a function
def f(x):
    return x*x

r = weakref.ref(f)
print(r)                # print the reference
print(r(5))             # call the function
print(r() is f)         # verify that the reference is to the original function

# Create a weak reference to a method
class C:
    def __init__(self, value):
        self.value = value
    def f(self):
        return self.value

c = C(10)
m = weakref.ref(c.f)

