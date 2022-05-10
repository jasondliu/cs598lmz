import codecs
# Test codecs.register_error() functionality.

import encodings

i = encodings.search_function("iso8859-1")(None, None)
o = encodings.search_function("utf-8")(None, None)
t = [
    (u"abc", "\x61\x62\x63"),
    (u"\xFF", ''.join([chr(x) for x in list(range(128))]) + '\xC3\xBF'),
    (u"\u0100", '\xC3\x81'),
    ]

def final(arg):
    assert arg == i
final_err = [final]

def ignore_error(exception):
    return (u"xy", 1)

def replace_error(exception):
    return (u"?", 1)

def xmlcharrefreplace_error(exception):
    return (u"&#%d;" % ord(exception.object[exception.start]), exception.end)

# This single codec error handler must be installed for the next few tests
encodings.register
