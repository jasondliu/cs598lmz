import gc, weakref

class Foo:
    def __init__(self, name):
        self.name = name
        print('Created a Foo object with name:', self.name)

    def __del__(self):
        print('Deleting a Foo object with name:', self.name)

def bar(name):
    return Foo(name)

f = bar('f')
b = bar('b')

# The reference count of f and b is 2
