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
else:
    raise Exception("Expected a LookupError")
# Test codecs.register_error() with a TypeError.
def type_error(name):
    return 1

try:
    codecs.register_error('test.typeerror', type_error)
except TypeError as e:
    print("Expected:", e)
else:
    raise Exception("Expected a TypeError")
# Test codecs.register_error() with an AttributeError.
def attribute_error(name):
    return lambda x: x

try:
    codecs.register_error('test.attrerror', attribute_error)
except AttributeError as e:
    print("Expected:", e)
else:
    raise Exception("Expected an Att
