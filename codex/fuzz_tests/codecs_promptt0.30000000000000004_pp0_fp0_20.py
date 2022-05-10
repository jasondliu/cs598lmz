import codecs
# Test codecs.register_error()

# This tests that the 'replace' error handler is registered by default.
# It also tests that the 'ignore' error handler is registered.

import codecs

def test(name):
    try:
        codecs.lookup_error(name)
    except LookupError:
        print "Error handler '%s' is not registered" % name
    else:
        print "Error handler '%s' is registered" % name

test('replace')
test('ignore')

# This tests that the 'xmlcharrefreplace' error handler is registered.

import codecs

def test(name):
    try:
        codecs.lookup_error(name)
    except LookupError:
        print "Error handler '%s' is not registered" % name
    else:
        print "Error handler '%s' is registered" % name

test('xmlcharrefreplace')

# This tests that the 'backslashreplace' error handler is registered.

import codecs

def test(name):
    try:
        codecs.lookup_error(
