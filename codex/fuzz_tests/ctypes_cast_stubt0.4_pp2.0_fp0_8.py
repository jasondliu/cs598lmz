import ctypes
ctypes.cast(id(x), ctypes.py_object).value

# This is the same as x.__dict__

# The __dict__ attribute is a dictionary object containing all the attributes of the class.
# The __dict__ attribute is writable.
# You can add, remove or modify the attributes of a class using the standard dictionary methods.

# We can also use the __dict__ attribute to access the value of an attribute.
# If the attribute doesn’t exist, a KeyError is raised.

x.__dict__['name']

# The __dir__ method returns a list of all the attributes of the class.
# The list includes the attributes of the parent classes as well.

x.__dir__()

# The __doc__ attribute contains the docstring defined in the class.

x.__doc__

# The __module__ attribute contains the module in which the class is defined.

x.__module__

# The __class__ attribute contains the class to which the instance belongs.

x.__class__

# The __bases__ attribute contains a tuple of parent classes.


