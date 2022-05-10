import weakref
# Test weakref.ref() and weakref.proxy()

# Create a class with a method
class Foo:
    def __init__(self, name):
        self.name = name
