import _struct
# Test _struct.Struct.format_size()
print _struct.Struct('i').format_size('@')
print _struct.Struct('i').format_size('<')
print _struct.Struct('i').format_size('>')
print _struct.Struct('i').format_size('=')
print _struct.Struct('i').format_size('!')
print _struct.Struct('i').format_size('x')
try:
    print _struct.Struct('i').format_size('y')
except ValueError, e:
    print e
# Test _struct.Struct.size
print _struct.Struct('i').size
# Test _struct.Struct.__new__
try:
    _struct.Struct('i', 'j')
except TypeError, e:
    print e
# Test _struct.Struct.__init__
try:
    _struct.Struct('i').__init__('j')
except TypeError, e:
    print e
# Test _struct.Struct.pack
print _struct.Struct('i').pack(1)
try:
    print _struct.Struct('i').
