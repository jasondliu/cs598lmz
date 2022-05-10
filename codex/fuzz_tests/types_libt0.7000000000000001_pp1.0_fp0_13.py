import types
types.FunctionType = types.LambdaType = lambda x: False
sys.modules['__builtin__'].__import__ = import_hook

def import_hook(name, globals=None, locals=None, fromlist=None, level=-1):
    if name in _implicit_imports:
        return None
    try:
        return _builtin_import(name, globals, locals, fromlist, level)
    except ImportError as ie:
        if name in _ignore_imports:
            return None
        sys.stderr.write("%s\n" % (ie))
        sys.stderr.write(traceback.format_exc())
        exit(1)

_builtin_import = builtin_import

def execfile(fn):
    try:
        if sys.version_info[0] < 3:
            execfile_(fn)
        else:
            execfile_(fn, {'__builtins__': __builtins__})
    except Exception as e:
        sys.stderr.write("%s\n"
