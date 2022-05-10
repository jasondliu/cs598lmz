from _struct import Struct
s = Struct.__new__(Struct)
print(s)
s.__unpack_from__ = lambda *args: args
print(s.__unpack_from__('test'))
print(s.__unpack_from__('test'))
print(s.__unpack_from__('test'))

print(s.__unpack_from__('test'))
print(s.__unpack_from__('test'))
print(s.__unpack_from__('test'))

print(s.__unpack_from__('test'))
print(s.__unpack_from__('test'))
print(s.__unpack_from__('test'))
