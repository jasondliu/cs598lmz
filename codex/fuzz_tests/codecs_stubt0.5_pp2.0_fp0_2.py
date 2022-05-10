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

# The following tests are from http://bugs.python.org/issue5221
# Test 1
try:
    b'\xff'.decode('utf-16')
except UnicodeDecodeError as ex:
    print(ex)
    print(ex.object)
    print(ex.start)
    print(ex.end)
    print(ex.reason)

# Test 2
try:
    b'\xff\xff'.decode('utf-32')
except UnicodeDecodeError as ex:
    print(ex)
    print(ex.object)
    print(ex.start)
    print(ex.end)
    print(ex.reason)

# Test 3
try:
    b'\xff\xff\xff\xff'.decode('utf-32')
except UnicodeDecodeError as ex:
    print(ex)
    print(ex.object)
    print(ex.start)
    print(ex.end)
    print(ex.reason)

# Test 4
try:
    b'\xff\xff\xff\xff'.dec
