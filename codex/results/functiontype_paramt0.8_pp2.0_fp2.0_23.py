from types import FunctionType
list(FunctionType(m.func_code, m.func_globals, m.__name__, m.func_defaults, 
                  m.func_closure))

def function2Method(func, instance, typeofmethod):
    # from http://mikewatkins.ca/2008/11/29/python-decorators-and-descriptors/
    def method(*args, **kwargs):
        return func(*(instance,)+args, **kwargs)
    method.__name__ = func.__name__
    method.__doc__ = func.__doc__
    method.__dict__.update(func.__dict__)
    method.im_func = func
    method.im_self = instance
    return typeofmethod(method)

def decorator(dec_args):

    def add_attribute(func):

        def wrapper(*func_args, **func_kwargs):
            res = func(*func_args, **func_kwargs)
            return res

        wrapper.attr = dec_args
        return wrapper

    return add_attribute

# http://
