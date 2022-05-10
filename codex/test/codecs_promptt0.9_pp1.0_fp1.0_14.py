import codecs
# Test codecs.register_error('replace_replace', codecs.replace_replace)
# Test codecs.register_error('replace_replace', codecs.replace_replace)

def _complain_on_bad_utf8(message):
    if 'decoded str' not in message or 'unexpected code byte' not in message:
        return message
    # This is an ugly hack to work around a quirk in py.test and coverage.py.
    # sys.decode() is called when a codec returns a decoding error, and is
    # passed the message returned by the codec.  But when running py.test or
    # coverage.py, we get a single ' ascii' codec can't decode byte 0xe2 in
    # position blah blah blah: ordinal not in range(128)" error for every test
    # that raises an exception, even if the failure has nothing to do with the
    # exception's message.  This at least silences that exception.
    if message.endswith('(128)"'):
        return message
    # If we don't have UTF-8 somewhere, assume the text was written in the

