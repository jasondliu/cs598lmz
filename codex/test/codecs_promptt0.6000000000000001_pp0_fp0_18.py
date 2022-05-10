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

