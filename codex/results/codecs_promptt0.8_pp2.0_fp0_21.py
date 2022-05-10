import codecs
# Test codecs.register_error
import codecs
codecs.register_bad_error('test', lambda x: None)
try:
    codecs.register_bad_error('test', lambda x: None)
except ValueError:
    pass
# Test codecs.register_error
import codecs
codecs.register_error('test', lambda x: None)
try:
    codecs.register_error('test', lambda x: None)
except ValueError:
    pass
