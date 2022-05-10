import types
# Test types.FunctionType
def handle_exception(f, t=Exception):
    def _wrapper(*args, **kwds):
        try: return f(*args, **kwds)
        except t, e: log.error("%s while accessing '%s': %s"%(t, f.func_name, e))
    return _wrapper
type(handle_exception)

method_registry = {}

def method(key, *args, **kwds):
    f = args[0]
    if not issubclass(f.__class__, types.FunctionType):
        raise Exception("Method decorator must be used on functions.")
    if not method_registry.has_key(key):
        method_registry[key] = []
    method_registry[key].append(f)

#__all__ = ["method", "method_registry"]
##
# end basic boiler plate


# Module 'upload'

##
# Function calls
##

def single(store, kwds):
    """
    Decorator method
    store: a Store
   
