import weakref
# Test weakref.ref().
class MyClass:
    def __init__(self, name):
        self.name = name
    def hi(self):
        print("hello", self.name)

obj = MyClass("Lethe")
r = weakref.ref(obj)
obj.hi()
obj = None
r().hi()

print(r())

print(r())

print(weakref.ref(r()) == weakref.ref(r()))

 
# Test weakref.proxy().
import weakref

class Example:
    def __init__(self, name):
        self.name = name
    def hi(self):
        print("Hello, %s!" % self.name)

obj = Example("World")
pr = weakref.proxy(obj)

print(type(pr))

print(type(obj))

print(pr == obj)

print(pr is obj)
