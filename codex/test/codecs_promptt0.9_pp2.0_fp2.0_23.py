import codecs
# Test codecs.register_error()

def lookup_error(name):
    desc = codecs.lookup_error(name)
    print(name, '\n  -->', desc)
    if isinstance(desc, codecs.CodecInfo):
        return desc

class foo:
    def __str__(self):
        return "foo"

# Test if we can work with exceptions not derived from Exception
try:
    lookup_error(foo())
except:
    pass

# Check if we can pass a None value
try:
    lookup_error(None)
except:
    pass
    
# Closing a nonexistent file shouldn't fail
