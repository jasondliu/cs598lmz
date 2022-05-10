import codecs
# Test codecs.register_error for BadNameError
try:
    codecs.register_error(name='NoSuchThing', error=ValueError)
except TypeError:
    print('SKIP')
    raise SystemExit

# Test codecs.register_error for an existing name
import encodings.ascii

assert codecs.register_error('strict', ValueError)
assert codecs.register_error('strict', encodings.ascii.replace_errors)

# Register non-callable non-exception; should error on codec lookup
try:
    codecs.register_error('offending_codec', 0)
except Exception:
    pass
else:
    print("Didn't raise error")

try:
    codecs.lookup("blah")
except LookupError:
    pass
else:
    print("Didn't raise error")

# Test u'\xb1'.encode('cp1252') will throw LookupError for offending_codec
