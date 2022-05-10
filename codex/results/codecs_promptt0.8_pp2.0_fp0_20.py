import codecs
# Test codecs.register_error()
import _testcapi
print 'default:'
print codecs.register_error('strict', codecs.strict_errors)
print codecs.register_error('ignore', codecs.ignore_errors)
print codecs.register_error('replace', codecs.replace_errors)
print codecs.register_error('xmlcharrefreplace', codecs.xmlcharrefreplace_errors)
print codecs.register_error('backslashreplace', codecs.backslashreplace_errors)
print codecs.register_error('namereplace', codecs.namereplace_errors)
print
errors = [x for x in dir(codecs) if x.endswith('_errors')]
for error in errors:
    error_class = getattr(codecs, error)
    print error + ':', codecs.register_error(error, error_class)
print
print 'Test surrogateescape'
codecs.register_error('surrogateescape', codecs.surrogateescape_errors)
utf8_source_text = '\\U0001d120\\U0001
