import codecs
# Test codecs.register_error
def strict_error_handler(message):
    raise UnicodeError(message)

def ignore_error_handler(message):
    return (u'', message.start + 1)

def replace_error_handler(message):
    return (u'\ufffd', message.start + 1)

def xmlcharrefreplace_error_handler(message):
    return (u'&#%d;' % ord(message.object[message.start]), message.start + 1)

def backslashreplace_error_handler(message):
    return (u'\\x%02x' % ord(message.object[message.start]), message.start + 1)

