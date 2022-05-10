import codecs
# Test codecs.register_error
import codecs
def my_handler(exc):
    raise TypeError
codecs.register_error('my.error', my_handler)
try:
    codecs.register_error('my.error', my_handler)
except Exception as exc:
    print(exc)
try:
    codecs.register_error(None, my_handler)
except Exception as exc:
    print(exc)
try:
    codecs.register_error('my.error', None)
except Exception as exc:
    print(exc)
try:
    codecs.register_error('my.error', lambda x: x)
except Exception as exc:
    print(exc)
# Test codecs.lookup_error
import codecs
def my_handler(exc):
    raise TypeError
codecs.register_error('my.error', my_handler)
codecs.lookup_error('my.error')
try:
    codecs.lookup_error(None)
except Exception as exc:
    print(exc)
# Test codecs.register_error() raise
