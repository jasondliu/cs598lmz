import codecs
# Test codecs.register_error('test', codecs.replace_errors)
# codecs.register_error('test', codecs.ignore_errors)

def test_codecs(encoding):
    try:
        # Test codecs.register_error('test', codecs.replace_errors)
        codecs.register_error('test', codecs.ignore_errors)
        print(encoding, '->', end=' ')
        print(codecs.encode(b'abc\xff', encoding, 'test'))
    except Exception as err:
        print('ERROR:', err)

if __name__ == '__main__':
    test_codecs('latin-1')
    test_codecs('utf-8')
