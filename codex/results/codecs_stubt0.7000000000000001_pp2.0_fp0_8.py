import codecs

def add_one_codepoint(exc):
    return ("a", exc.start)

def add_utf16_bytes(exc):
    return (b'ab', exc.start)

def add_utf32_bytes(exc):
    return (b'abcd', exc.start)

codecs.register_error("add_one_codepoint", add_one_codepoint)
codecs.register_error("add_utf16_bytes", add_utf16_bytes)
codecs.register_error("add_utf32_bytes", add_utf32_bytes)

def Test(tester):
    tester.startGroup('codecs')
    tester.startGroup('UTF-8')
    try:
        codecs.decode('abc\xed\xa0\x80', 'utf-8', 'strict')
        tester.error('UTF-8 strict -- should have raised an exception')
    except ValueError:
        pass
    else:
        tester.error('UTF-8 strict -- should have raised an exception')
    tester.test(codecs.decode('abc\xed\xa0\x80def', 'utf-8', 'replace'),
                'abc\uFFFddef')
    tester.test(codecs.decode('abc\xed\xa0def', 'utf-8', 'replace'),
                'abc\uFFFDdef')
    tester.test(codecs.decode('abc\xed\xa0\x80def', 'utf-8', 'ignore'),
                'abcdef')
    tester.test(codecs.decode('abc\
