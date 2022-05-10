import gc, weakref, warnings

# The next four functions are imported and used from the Python stdlib


def __get_builtin__(name):
    import __builtin__
    return getattr(__builtin__, name)

def __import__(name, globals=None, locals=None, fromlist=[]):
    if globals is None:
        globals = sys._getframe(1).f_globals
    if locals is None:
        locals = sys._getframe(1).f_locals
    if fromlist:
        level = 0
        for mod in fromlist:
            if locals.has_key(mod) or globals.has_key(mod):
                level = level + 1
    else:
        level = -1
    return getattr(__import__(name, globals, locals, fromlist, level), name)

def __reload__(module):
    import imp
    imp.reload(module)

def __unload__(name):
    import sys, imp
    for k, v in sys.modules.items():
       
