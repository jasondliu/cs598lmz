from _struct import Struct
s = Struct.__new__(Struct)
print Struct.__dict__.keys()
print Struct
print str(Struct)
print s
print str(s)
try:
  s.pack('=i')
  print 'failed!'
except TypeError, t:
  pass
print

s = Struct('=i')
try:
  s.pack(None)
  print 'failed!'
except TypeError, t:
  pass
print

s = Struct('=c')
try:
  s.pack('abc')
  print 'failed!'
except error, t:
  pass
print

s = Struct('=i')
try:
  s.pack('abc')
  print 'failed!'
except error, t:
  pass
print

s = Struct('=c')
try:
  s.pack('a', 'b')
  print 'failed!'
except error, t:
  pass
print

##if __name__ == '__main__': print 'main'
##if __name__ == 'test_struct': print 'test_struct'
##if __name__ == 'test_
