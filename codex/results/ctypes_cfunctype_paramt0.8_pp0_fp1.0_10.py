import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)

def load(name, e, globals=None):
    if globals is None:
        import __main__
        globals = __main__.__dict__
    mod = imp.new_module(name)
    mod.__file__ = "<%s>" % name
    mod.__dict__.update(globals)
    try:
        exec e in mod.__dict__
    except:
        sys.modules.pop(name)
        raise
    sys.modules[name] = mod
    return mod
