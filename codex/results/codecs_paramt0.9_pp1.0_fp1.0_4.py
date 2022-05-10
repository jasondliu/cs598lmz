import codecs
codecs.register_error('test-ignore', codecs.ignore_errors)
codecs.register_error('test-replace', codecs.replace_errors)
codecs.register_error('test-xmlcharref', codecs.xmlcharrefreplace_errors)

unicode_tests = [
    (b'abc\xe4\xe4\xe4\xe4def', 'ascii', 'test-replace', 'abc\ufffd\ufffd\ufffd\ufffddef'),
    (b'abc\xe4\xe4\xe4\xe4def', 'ascii', 'test-xmlcharref', 'abc&#228;&#228;&#228;&#228;def'),
    (b'abc\xe4\xe4\xe4\xe4def', 'latin-1', 'strict', 'abcäääädef'),
    (b'abc\xe4\xe4\xe4\xe4def', 'latin-1', 'replace', 'abc\ufffd\ufffddef'),
    (b'ab\xa2c', 'latin-
