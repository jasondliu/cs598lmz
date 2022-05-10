import codecs
# Test codecs.register_error()

import codecs

def my_error(exception):
    return (u"", exception.start + 1)

codecs.register_error("test.myerror", my_error)

# Error handling callback is called with a UnicodeDecodeError
# exception as argument, and must either raise this exception,
# or return a tuple (replacement, new position)

def my_error2(exception):
    return (u"", exception.start + 1)

codecs.register_error("test.myerror2", my_error2)

# Error handling callback is called with a UnicodeEncodeError
# exception as argument, and must either raise this exception,
# or return a tuple (replacement, new position)

def my_error3(exception):
    return (u"", exception.end)

codecs.register_error("test.myerror3", my_error3)

# Error handling callback is called with a UnicodeTranslateError
# exception as argument, and must either raise this exception,
# or return a tuple (replacement, new position
