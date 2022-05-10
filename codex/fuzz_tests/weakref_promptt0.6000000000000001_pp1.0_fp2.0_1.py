import weakref
# Test weakref.ref

class Foo:

    def __init__(self):
        self.data = 0

    def __del__(self):
        print('Foo.__del__')

class Bar:

    def __init__(self):
        self.data = 0

    def __del__(self):
        print('Bar.__del__')

f = Foo()
b = Bar()

print(f.data, b.data)

f.data = 1
b.data = 1

print(f.data, b.data)

x = weakref.ref(f)
y = weakref.ref(b)

del f
del b

print(x().data)
print(y().data)

# Test weakref.proxy

f = Foo()

x = weakref.proxy(f)

print(x.data)

f.data = 1

print(x.data)

del f

print(x.data)
