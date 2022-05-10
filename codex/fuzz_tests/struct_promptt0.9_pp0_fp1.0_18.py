import _struct
# Test _struct.Struct
s = _struct.Struct('i')
s.pack(1)
s[''] = 1
s = _struct.Struct('i', 'spam')
s[' '] = 1
s = _struct.Struct('i', (), True)
s = _struct.Struct('i', (), False, None)
s = _struct.Struct('i', (), False, None, amis=1)
# Constant test code
_struct.Struct('i')
_struct.Struct('i', 'spam')
_struct.Struct('i', 1)
_struct.Struct('i', 1, 1)
_struct.Struct('i', 1, 1, 1)
