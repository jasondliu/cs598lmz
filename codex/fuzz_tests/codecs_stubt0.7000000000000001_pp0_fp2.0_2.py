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

encoding = "utf-8"

# testing "strict"

def fn1(encoding):
    return codecs.getencoder(encoding)

def fn2(encoding):
    return codecs.getincrementalencoder(encoding)

def fn3(encoding):
    return codecs.getdecoder(encoding)

def fn4(encoding):
    return codecs.getincrementaldecoder(encoding)

def fn5(encoding):
    return codecs.getreader(encoding)

def fn6(encoding):
    return codecs.getwriter(encoding)

try:
    fn1(encoding)
except LookupError as e:
    print("fn1: ", e)

try:
    fn2(encoding)
except LookupError as e:
    print("fn2: ", e)

try:
    fn3(encoding)
except LookupError as e:
    print("fn3: ", e)

try:
    fn4(encoding)
