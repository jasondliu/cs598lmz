from types import FunctionType
list(FunctionType(lambda: None, {}).__code__.co_varnames)

# Is it a generator function?
def is_generator(obj):
    return isinstance(obj, types.GeneratorType)

# Is it a function?
def is_function(obj):
    return isinstance(obj, types.FunctionType)

# Is it a class?
def is_class(obj):
    return isinstance(obj, type)

# Is it an instance?
def is_instance(obj):
    return isinstance(obj, object)

# Is it a string?
def is_string(obj):
    return isinstance(obj, str)

# Is it a list?
def is_list(obj):
    return isinstance(obj, list)

# Is it a dictionary?
def is_dict(obj):
    return isinstance(obj, dict)

# Is it an iterable?
def is_iterable(obj):
    return isinstance(obj, collections.Iterable)

# Is it a file?
def is_file(obj):

