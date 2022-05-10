import types
# Test types.FunctionType
if not isinstance(dumps, types.FunctionType) or not isinstance(loads, types.FunctionType):
    raise ImportError
# Test presence of __doc__
if not dumps.__doc__ or not loads.__doc__:
    print __doc__
    raise ImportError(__doc__)
