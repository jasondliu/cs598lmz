fn = lambda: None
gi = (i for i in ())
fn.__code__ = code
sys.modules['gi'] = gi

# gi is the introspection module
# we hijack the __getattr__ to return the introspection module
# then we can get rid of the gi import in the library
gi.__getattr__ = lambda x: gi
for i in gi:
    sys.modules['gi.%s' % i] = gi

gi.__name__ = 'gi'
gi.__path__ = []
gi.__file__ = __file__
gi.__package__ = 'gi'
gi.__loader__ = None
