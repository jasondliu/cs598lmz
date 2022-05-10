import codecs
# Test codecs.register_error() and .name attributes to be present,
# even if none has been registered yet.
import codecs, copy
encodings = copy.copy(getattr(codecs, '__hooks__', {}))
for mod in encodings.values():
    mod = getattr(mod, '__loader__', mod)
    mod = getattr(mod, 'load_module', mod)
    mod('.test_codecs_none')

def test():
    #print 'registering', encoder
    r()
    r()
