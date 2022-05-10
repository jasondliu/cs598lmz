import codecs
# Test codecs.register_error.
codecs.register_error("test.unavailable", codecs.lookup_error("test.not_available"))
# Test codecs.lookup_error.
codecs.lookup_error("test.not_available")

# Test error instantiation.
try:
    raise UnicodeError('test.not_available')
except UnicodeError as e:
    print(e)
    print(e.encoding)
    print(e.reason)

[ c.decode() for c in [ bytearray([0x10, 0x20, 0x30]), bytes([0x10, 0x20, 0x30]), memoryview(bytearray([0x10, 0x20, 0x30])) ]]

# codecs module getencoder/getdecoder decorators
def codec_getencoder_decorator(fn):
    def wrapper(obj):
        print("codec_getencoder_decorator")
        return fn(obj)
    return wrapper

def codec_getdecoder_decorator(fn):
    def
