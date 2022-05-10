import types
types.ClassType = type
 
import inspect
def funcinfo(f):
    args, varargs, varkw, defaults = inspect.getargspec(f)
    name = getattr(f, "__name__", None)
    cls = getattr(f, "im_class", None)
    method = getattr(f, "im_func", None)
    methodname = getattr(method, "__name__", None)
    if cls and methodname:
        if name is None:
            name = "%s.%s" % (cls.__name__, methodname)
        method = "%s.%s" % (cls.__name__, methodname)
    elif methodname:
        if name is None:
            name = methodname
        method = methodname
    return args, varargs, varkw, defaults, name, method, cls
 
