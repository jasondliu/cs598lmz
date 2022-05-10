import codecs
# Test codecs.register_error()
def my_error(err):
    print(err)
codecs.register_error('CustomError', lambda err: (u'ERROR', err.end))
for encoding in ['rot13', 'utf-16']:
    codecs.register_error('CustomError', my_error)
