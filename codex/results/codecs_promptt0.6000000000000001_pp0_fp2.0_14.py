import codecs
# Test codecs.register_error()

# Test codecs.register_error()

import codecs
import sys

def handler(exception):
    return (u"", exception.end)

codecs.register_error("test.my_error", handler)

enc = codecs.getencoder("utf-8")

for i in range(0xD800, 0xDC00):
    try:
        enc(unichr(i), 'test.my_error')
    except UnicodeEncodeError, e:
        assert e.start == 0
        assert e.end == 1

# Test the "replace" error handler

for c in [u"\ud800", u"\udc00", u"\ufffd"]:
    assert enc(c, 'replace')[0] == "\xef\xbf\xbd"

# Test the "ignore" error handler

for c in [u"\ud800", u"\udc00", u"\ufffd"]:
    assert enc(c, 'ignore')[0] == ""

# Test UTF-8 B
