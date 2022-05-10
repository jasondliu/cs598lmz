import codecs
# Test codecs.register_error()

import codecs

def myfunc(message, errors='strict'):
    if message.startswith('x'):
        return (u'ERROR', message[2:])
    return 1, message[1:]

codecs.register_error('test.errors', myfunc)

def myencode(input, errors='strict'):
    import codecs
    return (input.replace('x', 'y'), len(input))

def mydecode(input, errors='strict'):
    import codecs
    return (input.replace('y', 'x'), len(input))

codecs.register(myencode, mydecode)

def foo(msg):
    try:
        u = u'a' + msg
        print repr(u.encode('test.errors'))
    except UnicodeEncodeError, err:
        print repr(err)

tests = [
    'xy',
    'x1\udcef',
    'x\udcef1',
    '\udcefx1',
]
