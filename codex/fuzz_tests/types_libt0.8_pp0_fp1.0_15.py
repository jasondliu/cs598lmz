import types
types.__setattr__(types.FunctionType, 'is_function', True)
@function
class myclass:
    def __init__(self):
        print "init"
    def __call__(self, *args, **kwargs):
        print 'called'
        return __builtin__.type.__call__(self, *args, **kwargs)
print(myclass.is_function)
print(myclass.__class__.__name__)
# a=myclass()
# a()

import importlib
importlib.reload(sys.modules[__name__])
