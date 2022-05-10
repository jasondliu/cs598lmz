import _struct
# Test _struct.Struct()
_struct.Struct('1s')
_struct.Struct('1s', 'utf-8')
_struct.Struct('1s', 'utf-16')
_struct.Struct('1s', 'utf-16-le')
_struct.Struct('1s', 'utf-16-be')
_struct.Struct('1s', 'utf-32')
_struct.Struct('1s', 'utf-32-le')
_struct.Struct('1s', 'utf-32-be')
# Test _struct.Struct.format
_struct.Struct('1s').format
_struct.Struct('1s', 'utf-8').format
_struct.Struct('1s', 'utf-16').format
_struct.Struct('1s', 'utf-16-le').format
_struct.Struct('1s', 'utf-16-be').format
_struct.Struct('1s', 'utf-32').format
_struct.Struct('1s', 'utf-32-le').format
_struct.Struct('1s', 'utf-32-be').format
# Test _struct.Struct.
