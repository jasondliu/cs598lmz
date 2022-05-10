import types
types.FunctionType = types.LambdaType

def _get_function_code(func):
    return func.__code__

def _get_function_defaults(func):
    return func.__defaults__

def _get_function_closure(func):
    return func.__closure__

def _get_function_globals(func):
    return func.__globals__

def _get_function_module(func):
    return func.__module__

def _get_function_dict(func):
    return func.__dict__

def _get_function_name(func):
    return func.__name__

def _get_function_qualname(func):
    return func.__qualname__

def _get_function_doc(func):
    return func.__doc__

def _get_function_annotations(func):
    return func.__annotations__

def _get_function_kwdefaults(func):
    return func.__kwdefaults__

def _set_function_closure(func,
