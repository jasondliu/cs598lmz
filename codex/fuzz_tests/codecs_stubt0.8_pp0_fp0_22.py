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

# test UTF-8
try:
    u"\x81".encode("utf-8")
except UnicodeEncodeError as e:
    r = e.reason
    if r != "invalid start byte" or e.start != 1:
        raise TestFailed("encoding error raised by UTF-8; "
                         "exception data: (%r, %d, %d)" % (e.reason, e.start, e.end))

# test UTF-16
try:
    u"\x81".encode("utf-16")
except UnicodeEncodeError as e:
    r = e.reason
    if r != "invalid continuation byte" or e.start != 1:
        raise TestFailed("encoding error raised by UTF-8; "
                         "exception data: (%r, %d, %d)" % (e.reason, e.start, e.end))

# test UTF-32
try:
    u"\x81".encode("utf-32")
except UnicodeEncodeError as e:
    r = e.reason
   
