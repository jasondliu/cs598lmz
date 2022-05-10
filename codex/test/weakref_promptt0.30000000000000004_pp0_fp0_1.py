import weakref
# Test weakref.ref() and weakref.proxy()

# Create a class with a __del__ method
class C:
    def __init__(self, name):
        self.name = name
