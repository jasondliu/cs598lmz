import weakref
# Test weakref.ref()

# Create a class with a __del__ method
class C:
    def __init__(self, arg):
        self.arg = arg
    def __del__(self):
        print("C.__del__", self.arg)

# Create an instance and a weak reference to it
x = C(1)
y = weakref.ref(x)
print("y:", y)
print("y():", y())

# Delete the instance
del x
print("y():", y())

# Create a new instance with the same id
x = C(2)
print("y():", y())

# Delete the instance again
del x
print("y():", y())

# Create a new instance with the same id
x = C(3)
print("y():", y())

# Delete the instance again
del x
print("y():", y())

# Create a new instance with the same id
x = C(4)
print("y():", y())

# Delete the instance again
del x
print("y():", y())

#
