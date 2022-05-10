import weakref
# Test weakref.ref(object)

def callback(obj):
    print("object is dead")

class Foo(object):
    def __del__(self):
        print("object is now dead")

a = Foo()
b = weakref.ref(a, callback)
print(b)

a = None
del a

# print(b())

print(b)


# Test weakref.ref(object, callback)

class Foo(object):
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print("object is now dead")

def callback(obj):
    print(obj.name, "is dead")

a = Foo("a")
b = weakref.ref(a, callback)

a = None
del a

print(b())
