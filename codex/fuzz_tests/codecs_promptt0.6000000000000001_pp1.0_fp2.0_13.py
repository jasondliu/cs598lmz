import codecs
# Test codecs.register_error
def bad_unicode(e):
    print('bad_unicode:', e)
    return ('',e.start + 1)
codecs.register_error('test.bad_unicode', bad_unicode)
for encoding in ['latin-1', 'utf-8', 'utf-16']:
    print('\nEncoding:', encoding)
    try:
        s = b'\x80abc'
        print(s.decode(encoding, 'test.bad_unicode'))
    except UnicodeDecodeError as err:
        print('ERROR:', err)

# Register an error handler that doesn't take an additional argument
def bad_unicode(e):
    print('bad_unicode:', e)
    return ('',e.start + 1)
codecs.register_error('test.bad_unicode', bad_unicode)
for encoding in ['latin-1', 'utf-8', 'utf-16']:
    print('\nEncoding:', encoding)
    try:
        s = b'\x80abc
