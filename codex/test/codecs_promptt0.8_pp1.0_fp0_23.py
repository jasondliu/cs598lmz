import codecs
# Test codecs.register_error()
# Register a handler that replaces data by "!"
def replace_handler(exc):
    return (u'!', exc.start + 1)
codecs.register_error('replace', replace_handler)
