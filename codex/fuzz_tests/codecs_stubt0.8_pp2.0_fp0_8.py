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

##a = u'abcd\N{SNOWMAN}'
##print(a.encode('utf-32-be', 'add_one_codepoint'))
##print(a.encode('utf-16-be', 'add_one_codepoint'))
##print(a.encode('utf-16-be', 'add_utf16_bytes'))
##print(a.encode('utf-32-be', 'add_utf32_bytes'))

##def replace_func(exc):
##    return ('?', exc.start)
##
##def replace_illegal_utf8(exc):
##    print(exc)
##    return ('?', exc.start)
##
##def error_handler(exc):
##    print(exc)
##    return (exc.start, exc.end)

##codecs.register_error("replace_func", replace_func)
##codecs.register_error("replace_illegal_utf8", replace_illegal_utf8)
##codecs.register_error("error_handler
