import codecs
# Test codecs.register_error()
codecs.register_error("errf", lambda x: (x, "err"))

def test_main():
    test_codec('utf-8')
    test_codec('utf-8-sig')
    test_codec('utf-16')
    test_codec('utf-16-le')
    test_codec('utf-16-be')
    test_codec('utf-32')
    test_codec('utf-32-le')
    test_codec('utf-32-be')

    test_codec('unicode_internal')

    test_codec('utf-7')
    test_codec('utf-8-variants')
    test_codec('utf-16-variants')
    test_codec('utf-32-variants')
    test_codec('utf-7-variants')

    test_codec('mbcs')
    test_codec('oem')

    test_codec('punycode')
    test_codec('idna')
