import codecs
# Test codecs.register_error()
#
# This test is for the codecs.register_error() function.
#
# The test is run by running this file as a script.
#
# Written by Marc-Andre Lemburg (mal@lemburg.com).

import codecs

#
# Test basic functionality

def test_basic():

    def replace_error(exc):
        if not isinstance(exc, UnicodeError):
            raise TypeError("don't know how to handle %r" % exc)
        return (u'*', exc.end)

    codecs.register_error('test.replace', replace_error)

    # Encode
    u = u'\u3042\u3044\u3046\u3048\u304a'
    s = u.encode('euc-jp', 'test.replace')
