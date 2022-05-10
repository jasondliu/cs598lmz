import types
# Test types.FunctionType if available (Python 2.2 and better), otherwise
# fall back to types.MethodType.
try:
    func_type = types.FunctionType
except AttributeError:
    func_type = types.MethodType

# check whether PYTHON_EGG_CACHE is set.  If so, honour it.
# this is needed for webware to work inside of an egg.
try:
    import os
    if 'PYTHON_EGG_CACHE' in os.environ:
        import sys
        sys.path.insert(0, os.environ['PYTHON_EGG_CACHE'])
except ImportError:
    pass

undefined = object()

class NotGiven(object):
    """Marker to indicate that a keyword argument has not been given.
    """
    
    def __repr__(self):
        return "NotGiven"

NotGiven = NotGiven()

def attr(obj, attrname, default=None):
    """Returns the value of the named attribute of the passed object or default
   
