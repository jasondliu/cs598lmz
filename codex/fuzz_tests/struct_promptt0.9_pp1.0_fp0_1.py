import _struct
# Test _struct.Struct('B')
c = _struct.Struct('B')
try:
   c.pack('')
except:
   print 'Pack fails with invalid format'

# Test _struct.Struct('x', 'd').unpack('xyz')
try:
   d = _struct.Struct('x', 'd')
   d.unpack('xyz')
except:
   print 'Unpack fails with invalid format'

# Test _struct.Struct('bb')
try:
   e = _struct.Struct('bb')
   e.unpack('xyz')
except:
   print 'Unpack fails with invalid format'

# Test _struct.Struct('s', 'd')
try:
   f = _struct.Struct('s', 'd')
   f.unpack('xyz')
except:
   print 'Unpack fails with invalid format'

# Test _struct.Struct('b').unpack_from('xyz')
try:
   g = _struct.Struct('b')
   g.unpack_from('xyz')
except:
   print 'Unpack
