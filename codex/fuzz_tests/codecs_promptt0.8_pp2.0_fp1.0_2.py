import codecs
# Test codecs.register_error
codecs.register_error('blah', codecs.replace_errors)
try:
    codecs.register_error('blah', codecs.replace_errors)
except ValueError:
    print('ValueError')

print(codecs.lookup_error('blah'))
try:
    codecs.lookup_error('blah2')
except LookupError:
    print('LookupError')

# Test name matching
assert codecs.lookup_error('ignore') is codecs.ignore_errors
assert codecs.lookup_error('replace') is codecs.replace_errors
assert codecs.lookup_error('xmlcharrefreplace') is codecs.xmlcharrefreplace_errors
assert codecs.lookup_error('strict') is codecs.strict_errors


# Test codecs.register_error(func)
try:
    codecs.register_error(codecs.replace_errors)
except TypeError:
    print('TypeError')

# Test that replace_errors[_handler] modifies the default encoding behavior
s
