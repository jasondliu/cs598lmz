import types
# Test types.FunctionType to detect function objects
def is_function(function):
    return type(function) == types.FunctionType

# Test types.ClassType to detect class objects
def is_class(klass):
    return type(klass) == types.ClassType

# Test types.InstanceType to detect instances of a class
def is_instance(instance):
    return type(instance) == types.InstanceType

# Test type of any object
def is_type(var):
    return isinstance(var, type)

# Return True if given object is a dictionary
def is_dict(var):
    return isinstance(var, dict)

# Return True if given object is a list or tuple
def is_list_or_tuple(var):
    return isinstance(var, (list, tuple))

# Return True if given object is a sequence
def is_iterable(var):
    return isinstance(var, collections.Iterable)

# Return True if given object is a string
def is_string(var):
    return isinstance(var, str)
