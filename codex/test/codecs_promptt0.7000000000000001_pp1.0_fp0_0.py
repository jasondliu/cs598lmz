import codecs
# Test codecs.register_error() with a lookup error.
class LookupError(Exception):
    pass

def lookup_error(name):
    raise LookupError(name)

try:
    codecs.register_error('test.lookuperror', lookup_error)
except LookupError as e:
    print("Expected:", e)
