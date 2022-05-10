import codecs
# Test codecs.register_error

import codecs

def bad_decode(input, errors='strict'):
    raise UnicodeError, "bad decode"

def bad_encode(input, errors='strict'):
    raise UnicodeError, "bad encode"

codecs.register_error('test.bad_decode', bad_decode)
codecs.register_error('test.bad_encode', bad_encode)

def test(name, input, errors='strict'):
    print '%s: %r' % (name, input)
    print '  strict:',
    try:
        print repr(input.encode(name, errors))
    except UnicodeError, detail:
        print 'ERROR:', detail
    print '  replace:', repr(input.encode(name, 'replace'))
    print '  ignore:', repr(input.encode(name, 'ignore'))
    print '  xmlcharrefreplace:', repr(input.encode(name, 'xmlcharrefreplace'))
    print '  bad_decode:', repr(
