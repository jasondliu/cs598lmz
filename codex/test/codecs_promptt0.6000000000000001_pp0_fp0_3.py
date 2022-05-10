import codecs
# Test codecs.register_error()
try:
    codecs.register_error('test.strict', codecs.strict_errors)
except (TypeError, ValueError):
    raise TestFailed("Test failed: 'test.strict' is a reserved error name")
try:
    codecs.register_error('test.strict', codecs.strict_errors)
except (TypeError, ValueError):
    raise TestFailed("Test failed: registering the same error function twice is not allowed")

def encoder(s):
    return s, len(s)

def decoder(s):
    return s, len(s)

try:
    codecs.register_error('test.pass_through', encoder)
except (TypeError, ValueError):
    raise TestFailed("Test failed: 'test.pass_through' is a reserved error name")

try:
    codecs.register_error('test.pass_through', decoder)
except (TypeError, ValueError):
    raise TestFailed("Test failed: registering the same error function twice is not allowed")

