import codecs
# Test codecs.register_error

# This test is not exhaustive.  It only tests the error handling
# mechanism, not the actual codecs.

import codecs
import sys

def test(name, input, errors, expected):
    print name, input, errors, expected
    got = codecs.decode(input, errors=errors)
    if got != expected:
        print 'expected:', repr(expected)
        print '     got:', repr(got)
        raise ValueError

def test_strict(input, expected):
    test('strict', input, 'strict', expected)

def test_ignore(input, expected):
    test('ignore', input, 'ignore', expected)

def test_replace(input, expected):
    test('replace', input, 'replace', expected)

def test_xmlcharrefreplace(input, expected):
    test('xmlcharrefreplace', input, 'xmlcharrefreplace', expected)

def test_backslashreplace(input, expected):
    test('backslashreplace', input, 'backslashreplace', expected)

def test_name
