import codecs
codecs.register_error('FooError', codecs.lookup_error('foo'))

print('-' * 55)
en, de = codecs.lookup('base64')

try:
    en.encode('blah')
except Exception as e:
    print(type(e), e)

print('-' * 55)
try:
    en.encode('blah', 'FooError')
except Exception as e:
    print(type(e), e)

print('-' * 55)
try:
    codecs.register_error('FooError', codecs.lookup_error('foo'))
except Exception as e:
    print(type(e), e)
