import codecs
# Test codecs.register_error

import codecs

def replace_error(exc):
    if isinstance(exc, UnicodeDecodeError):
        return (u'\ufffd', exc.end)
    else:
        raise TypeError("don't know how to handle %r" % exc)

codecs.register_error('test.replace', replace_error)

def test(encoding):
    print '-'*50
    print 'Encoding:', encoding
    print 'encode:', repr(u'\u3042\u3044\u3046\u3048\u304a')
    print 'decode:', repr('\xff\xfe\x30\x42\x30\x44\x30\x46\x30\x48\x30\x4a')
    print '-'*50
    print 'Without error handler:'
    try:
        print 'encode:', repr(u'\u3042\u3044\u3046\u3048\u304a'.encode(encoding))
    except UnicodeEncodeError, err:
       
