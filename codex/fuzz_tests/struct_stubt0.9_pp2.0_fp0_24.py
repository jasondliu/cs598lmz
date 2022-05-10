from _struct import Struct
s = Struct.__new__(Struct)

# s.format
print('_struct.__doc__=', Struct.__doc__)
print('s.__doc__=', s.__doc__)
print('s.__dict__=', s.__dict__)
print('s.__str__=', s.__str__)
print('s.__dir__=', s.__dir__)
print('s.__name__=', s.__name__)
print('s.__new__=', s.__new__)
print('s._formats_by_size=', s._formats_by_size)
print('s._map=', s._map)
print('s.format=', s.format)

# s._formats_by_size
