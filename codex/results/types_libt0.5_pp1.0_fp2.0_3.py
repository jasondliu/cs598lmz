import types
types.ModuleType.__bases__ += (object,)

def _reload(module):
    reload(module)
    return module

def _import(name):
    __import__(name)
    return sys.modules[name]

def _reload_import(name):
    return _reload(_import(name))

def _import_from(name, fromlist):
    mod = _import(name)
    for x in fromlist:
        setattr(mod, x, getattr(mod, x))
    return mod

def _reload_import_from(name, fromlist):
    return _reload(_import_from(name, fromlist))

def import_module(name, package=None):
    """Import a module.

    The 'package' argument is required when performing a relative import. It
    specifies the package to use as the anchor point from which to resolve the
    relative import to an absolute import.

    """
    if name.startswith('.'):
        if not package:
            raise TypeError("relative imports require the 'package' argument")
