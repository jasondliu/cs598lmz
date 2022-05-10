import codecs
# Test codecs.register_error()
codecs.register_error('test.strict', codecs.strict_errors)
codecs.register_error('test.replace', codecs.replace_errors)
codecs.register_error('test.ignore', codecs.ignore_errors)
codecs.register_error('test.xmlcharrefreplace', codecs.xmlcharrefreplace_errors)
codecs.register_error('test.backslashreplace', codecs.backslashreplace_errors)
# Test codecs.lookup_error()
for name in ['strict', 'replace', 'ignore', 'xmlcharrefreplace', 'backslashreplace']:
    assert codecs.lookup_error('test.' + name) == getattr(codecs, name + '_errors')
# Test non-standard error handlers
def bad_errorhandler(exception):
    raise RuntimeError("This shouldn't be called")

codecs.register_error('test.bad', bad_errorhandler)
try:
    'xx'.encode('ascii', 'test.bad')
    assert
