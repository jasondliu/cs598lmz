import _struct
# Test _struct.Struct.
TestError( _struct.calcsize('12'), 1, '_struct.calcsize(\'12\')' )
TestError( _struct.calcsize(''), 0, '_struct.calcsize(\'\')' )
TestError( _struct.calcsize('@'), 0, '_struct.calcsize(\'@\')' )
TestError( _struct.calcsize('=@'), 0, '_struct.calcsize(\'=@\')' )
TestError( _struct.calcsize('=@3'), 0, '_struct.calcsize(\'=@\')' )
TestError( _struct.calcsize('=@3i'), 12, '_struct.calcsize(\'=@3i\')' )
TestError( _struct.calcsize('=@3i5'), 12, '_struct.calcsize(\'=@3i5\')' )
TestError( _struct.calcsize('=@3i5c'), 13, '_struct.calcsize(\'=@3i5
