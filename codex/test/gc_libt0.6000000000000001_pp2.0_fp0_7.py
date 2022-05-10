import gc, weakref

def func_name(f):
    """Find the name of a function or class"""
    if hasattr(f, 'func_name'):
        return f.func_name
    elif hasattr(f, 'im_class'):
        return f.im_class.__name__ + '.' + f.im_func.func_name
    else:
        return str(f)

def _wrapped_func_name(func):
    if hasattr(func, 'im_func'):
        return func.im_func.func_name
    return func.func_name

def _wrapped_func_class(func):
    if hasattr(func, 'im_class'):
        return func.im_class
    return None

def _wrapped_func_self(func):
    if hasattr(func, 'im_self'):
        return func.im_self
    return None

def _wrapped_func_module(func):
    if hasattr(func, 'func_module'):
        return func.func_module

