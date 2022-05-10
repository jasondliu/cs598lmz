from types import FunctionType
list(FunctionType(function_code).__code__.co_varnames)

"""

# Function to get the name of the function that created the object
def get_calling_function_name(level=1):
    return inspect.stack()[level][3]

# Function to get the name of the module that created the object
def get_calling_module_name(level=1):
    return inspect.stack()[level][1]

# Function to get the name of the module that created the object
def get_calling_module_path(level=1):
    return inspect.stack()[level][1].split('/')[-1]

# Function to get the line number of the function that created the object
def get_calling_line_number(level=1):
    return inspect.stack()[level][2]

# Function to get the name of the object
def get_object_name(object):
    return object.__name__

# Function to get the name of the class
def get_class_name(object):
    return object.__class__.__name__

#
