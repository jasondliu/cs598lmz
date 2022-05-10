from _struct import Struct
s = Struct.__new__(Struct)
s.__setattr__('format', 'i')
dumps = [x for x in s._formats_from_format("i")]
print(dumps)
