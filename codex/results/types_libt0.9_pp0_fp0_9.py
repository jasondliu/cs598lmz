import types
types.ModuleType('starpy.manager')

def __getattr__(name):
    import sys
    return getattr(sys.modules['starpy.manager'], name)

# end of class manager
manager = manager()
