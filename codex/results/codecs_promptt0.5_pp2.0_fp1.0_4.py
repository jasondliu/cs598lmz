import codecs
# Test codecs.register_error()

import codecs
import sys

def print_unicode(s, name):
    print '%s: %s' % (name, repr(s))
    for c in s:
        print '%s: %x' % (name, ord(c))

def register_error(encoding):
    def ignore_errors(error):
        print 'ignore_errors:', error.__class__
        return (u'\ufffd', error.start + 1)

    def replace_errors(error):
        print 'replace_errors:', error.__class__
        return (u'\ufffd', error.start + 1)

    def xmlcharrefreplace_errors(error):
        print 'xmlcharrefreplace_errors:', error.__class__
        return (u'&#%d;' % ord(error.object[error.start]), error.start + 1)

    def backslashreplace_errors(error):
        print 'backslashreplace_errors:', error.__class__
        return (u'\\x%02x' % ord(error
