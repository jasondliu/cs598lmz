import ctypes
# Test ctypes.CField

# This test is a bit tricky.  We need to create a class with a
# ctypes.CField attribute, and then we need to create an instance of
# that class.  We can't just create an instance of the class and then
# add the attribute, because the attribute is a descriptor, and
# descriptors only work on class attributes.  So we need to create a
# class with the attribute, and then create an instance of that class.
#
# We can't do that in a function, because the class will go out of
# scope and be garbage collected when the function returns.  So we
# need to create the class in the global scope, and then create an
# instance of that class.
#
# We can't do that in a module, because the module will be garbage
# collected when the test finishes.  So we need to create the class in
# the global scope of a module, and then create an instance of that
# class.
#
# So we create a module, and then create a class in the global scope
# of that module, and then create an instance of that class.

# Create a module
