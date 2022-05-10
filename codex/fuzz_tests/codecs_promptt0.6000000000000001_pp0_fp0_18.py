import codecs
# Test codecs.register_error()
#

import codecs

def my_replace(str, errors="strict"):
    return u"\uFFFD", str[1:]

def my_ignore(str, errors="strict"):
    return u"", str[1:]

def my_strict(str, errors="strict"):
    raise UnicodeError("strict error handler")

def my_error(str, errors="strict"):
    raise UnicodeError("my error handler")

def test():
    # test UnicodeEncodeError handling
    #
    # 1. default "strict"
    try:
        unicode("abc\xFF", "ascii")
    except UnicodeError, x:
        print "default strict", x
    else:
        print "default strict - no exception"

    # 2. "replace"
    codecs.register_error("test.replace", my_replace)
    print repr(unicode("abc\xFF", "ascii", "test.replace"))

    # 3. "ignore"
    codecs.register_error("
