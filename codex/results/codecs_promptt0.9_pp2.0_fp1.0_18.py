import codecs
# Test codecs.register_error for value errors.



# Change the behaviour of a registered error handler.  See issue #17270
import email
import codecs
def handle_special(exc):
    return (b"ignored", exc.end)
codecs.register_error("ignore", handle_special)
msg = email.message_from_file(codecs.open("non-ascii-header.eml",
                                          encoding="cp65001", errors="ignore"))
msg.get('From')
# msg.get_payload()

import sys
# codecs.register_error("test", None)


# test codecs.escape_decode
def f(a, b):
    print('f called with', a, b)
s = b'abc'
codecs.escape_decode(s, 'strict', f)
codecs.escape_decode(s, 'strict', f, 1)
codecs.escape_decode(s, 'strict', f, 1, b'A')
codecs.escape_decode(s, 'st
