import _struct
# Test _struct.Struct.__new__ with keyword arguments.
_struct.Struct('i').__new__(format='i')
_struct.Struct('i').__new__(format='i', byteorder='@')
_struct.Struct('i').__new__(format='i', byteorder='@', _silent=False)
_struct.Struct('i').__new__(format='i', byteorder='@', _silent=False, _aligned=False)
_struct.Struct('i').__new__(format='i', byteorder='@', _silent=False, _aligned=False,
                            _anonymous=False)

# Test _struct.Struct.__new__ with positional arguments.
_struct.Struct.__new__(_struct.Struct, 'i')
_struct.Struct.__new__(_struct.Struct, 'i', '@')
_struct.Struct.__new__(_struct.Struct, 'i', '@', False)
_struct.Struct.__new__(_struct.Struct, 'i', '@', False, False)
