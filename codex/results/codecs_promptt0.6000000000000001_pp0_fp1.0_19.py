import codecs
# Test codecs.register_error()

import codecs

def my_error_func(e):
  print 'my_error_func:', str(e)
  return u'\ufffd', e.end

def test(encoding):
  print '-*'*25
  print 'encoding:', encoding
  print '-*'*25
  codecs.register_error('test.my_error', my_error_func)
  print 'default encoding error handler:', \
        codecs.lookup_error('strict')
  print '-*'*25
  print '+'*40
  print 'use default error handler'
  print '+'*40
  t = codecs.getencoder(encoding)
  s = u'\u3042\u3044\u3046\u3048\u304a'
  print 'INPUT:', repr(s), type(s)
  print 'OUTPUT:', repr(t(s)[0]), type(t(s)[0])
  print '-*'*25
  print '+'
