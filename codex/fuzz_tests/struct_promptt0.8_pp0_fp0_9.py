import _struct
# Test _struct.Struct.__init__
_struct.Struct
_struct.Struct('i')
_struct.Struct('hhi')
_struct.Struct('hhhi')
_struct.Struct('hhhi', True)
_struct.Struct('hhhi', True, '<')
_struct.Struct('hhhi', True, '>')
# struct.Struct('hhhi', True, '=')
_struct.Struct('hhhi', False, '<')
_struct.Struct('hhhi', False, '>')
# struct.Struct('hhhi', False, '=')
try:
    _struct.Struct('hhhi', False, 'x')
except ValueError:
    pass
else:
    raise TestFailed('ValueError not raised')
try:
    _struct.Struct('hhhi', 'f')
except TypeError:
    pass
else:
    raise TestFailed('TypeError not raised')
try:
    _struct.Struct('hhhi', 'True')
except TypeError:
    pass
else:
    raise TestFailed('TypeError not raised')
try:
    _struct
