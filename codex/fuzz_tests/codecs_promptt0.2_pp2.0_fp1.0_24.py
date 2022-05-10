import codecs
# Test codecs.register_error

def handler(exception):
    return (u'', exception.end)

codecs.register_error('test.strict', handler)

# Test codecs.lookup_error

def test(name):
    print '%s: %s' % (name, codecs.lookup_error(name))

test('strict')
test('ignore')
test('replace')
test('xmlcharrefreplace')
test('test.strict')

# Test codecs.strict_errors

def test(name):
    print '%s: %s' % (name, codecs.strict_errors(name))

test('strict')
test('ignore')
test('replace')
test('xmlcharrefreplace')
test('test.strict')

# Test codecs.ignore_errors

def test(name):
    print '%s: %s' % (name, codecs.ignore_errors(name))

test('strict')
test('ignore')
test('replace')
test('xmlcharrefreplace')
test('test
