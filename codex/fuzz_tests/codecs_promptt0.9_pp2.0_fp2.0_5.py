import codecs
# Test codecs.register_error


errmods = map(__import__, ['encodings.undefined', 'encodings.backslashreplace',
    'encodings.replace', 'encodings.xmlcharrefreplace',
    'encodings.nameprep', 'encodings.punycode'])

for errmod in errmods:
    reload(errmod)


def test():
    for errmod in errmods:
        err = errmod.Codec().encode(u'\ud800')
        codecs.register_error(errmod.__name__, errmod.Codec().encode)
        exc = None
        try:
            codecs.decode(err, 'ascii', errmod.__name__)
        except UnicodeError, exc:
            pass
        else:
            raise AssertionError('error handler %s not called' % errmod.__name__)


def test_main():
    test()
    test()


if __name__ == '__main__':
    test_main()
