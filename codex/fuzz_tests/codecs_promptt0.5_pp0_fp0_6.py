import codecs
# Test codecs.register_error
def my_error(exception):
    return (u'', exception.end)
codecs.register_error('myerror', my_error)

print(codecs.lookup_error('myerror'))

codecs.register_error('myerror', codecs.strict_errors)
print(codecs.lookup_error('myerror'))

codecs.register_error('myerror', codecs.replace_errors)
print(codecs.lookup_error('myerror'))

codecs.register_error('myerror', codecs.ignore_errors)
print(codecs.lookup_error('myerror'))

codecs.register_error('myerror', codecs.xmlcharrefreplace_errors)
print(codecs.lookup_error('myerror'))

codecs.register_error('myerror', codecs.backslashreplace_errors)
print(codecs.lookup_error('myerror'))

codecs.register_error('myerror', codecs
