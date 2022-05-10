import codecs
# Test codecs.register_error:
def raise_error(exception):
    raise exception
codecs.register_error('test.lookup', raise_error)
codecs.lookup_error('test.lookup')

# Test codecs.register_error:
def raise_error(exception):
    raise exception
codecs.register_error('test.lookup', raise_error)
codecs.lookup_error('test.lookup')

# Test codecs.lookup_error:
from codecs import lookup_error
