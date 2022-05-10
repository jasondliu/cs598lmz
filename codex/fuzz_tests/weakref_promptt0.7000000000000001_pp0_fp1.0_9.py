import weakref
# Test weakref.ref() and weakref.proxy()

# Make a class with a couple of methods

class Foo:
    def __init__(self):
        self.msg = "Foo instance"

    def bar(self):
        return "Bar method of " + self.msg

# Create a Foo instance

f = Foo()

# Create a weakref to it

f_ref = weakref.ref(f)

# Create a weakproxy, also with a method

f_proxy = weakref.proxy(f)

# Print the instance method

print(f_proxy.bar())

# Print the proxy method

print(f_proxy.bar)

# Delete the instance

del f

# Print the proxy method

print(f_proxy.bar)

# Try the instance method

print(f_proxy.bar())
