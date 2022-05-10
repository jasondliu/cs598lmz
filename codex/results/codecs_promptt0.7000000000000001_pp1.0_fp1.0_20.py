import codecs
# Test codecs.register_error function
# It is a function.
assert callable(codecs.register_error)
# It accepts three parameters.
assert codecs.register_error.__code__.co_argcount == 3
# It is a function that takes a function as parameter.
codecs.register_error('test.test_codecs', lambda x: (x, x))
codecs.register_error('test.test_codecs', lambda x: (x, x), 'ignore')
codecs.register_error('test.test_codecs', lambda x: (x, x), 'replace')
codecs.register_error('test.test_codecs', lambda x: (x, x), 'xmlcharrefreplace')
# It can not accept other parameters.
with raises(TypeError):
    codecs.register_error('test.test_codecs', lambda x: (x, x), 'ignore', 'a_string')
# It raise error if the error handler is not a callable.
with raises(TypeError):
    codecs.register_error('test.test
