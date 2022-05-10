import types
# Test types.FunctionType and types.BuiltinFunctionType
# for availability.
try:
    types.FunctionType
except AttributeError:
    types.FunctionType = None
try:
    types.BuiltinFunctionType
except AttributeError:
    types.BuiltinFunctionType = None

_MISSING = object()

def setdefault(obj, key, default=None):
    if key in obj:
        return obj[key]
    else:
        obj[key] = default
        return default

def _resolve_name(name, package, level):
    """Return the absolute name of the module to be imported."""
    if not hasattr(package, 'rindex'):
        raise ValueError("'package' not set to a string")
    dot = len(package)
    for x in xrange(level, 1, -1):
        try:
            dot = package.rindex('.', 0, dot)
        except ValueError:
            raise ValueError("attempted relative import beyond top-level "
                              "package")
    return "%s.%s" % (
