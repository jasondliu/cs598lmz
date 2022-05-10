from types import FunctionType
list(FunctionType(lambda: None).__globals__.keys())

# ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__annotations__', '__builtins__', '__file__', '__cached__', 'types']

# The os module is not in the list because it is not accessible from the function.

# We can also see that the __file__ and __cached__ attributes are set.
# These attributes are set by the import machinery when a module is imported.

# The __file__ attribute is the path to the source file from which the module was imported.
# In this case, it is the path to the file we created.

# The __cached__ attribute is used only for modules that are imported from a .pyc file.
# It contains the path to the .pyc file.
# If the module was imported from a .py file, the __cached__ attribute is not set.

# The __file__ and __cached__ attributes are not included in the __dict__ attribute of a module.

# In addition to the attributes
