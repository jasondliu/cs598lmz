import codecs
# Test codecs.register_error
import _codecs
a = 'abc'
b = a.encode('unicode_escape', 'ignore')
if b != b'abc':
    #print '1'
    raise RuntimeError
if a.encode('unicode_escape', 'ignore') != b:
    #print '2'
    raise RuntimeError

def my_exc(exc):
    return (True, None)

codecs.register_error('test.ignore', my_exc)

c = a.encode('unicode_escape', 'test.ignore')
if c != b'abc':
    #print '3'
    raise RuntimeError

# Issue #9317 : make sure that the error handler
# sees the "real_errors" argument of the builtin encode()
# methods of str and unicode.
# See http://bugs.python.org/issue9317.

def my_exc2(exc):
    return (True, exc.end + 1)

a = '\x80x'
