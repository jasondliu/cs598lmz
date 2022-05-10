from _struct import Struct
s = Struct.__new__(Struct)

for key, value in vars(Struct).iteritems():
    if type(value) == types.FunctionType:
        setattr(s, key, types.MethodType(value, s, Struct))

s.format = 'I 2s f'
s.size = s.calcsize(s.format)
                                                                                
discard, member1, member2, member3 = s.unpack(b'\x00\x00\x00\x01\x00\x02\x00\x03')

print '%s\n  %s\n  %s\n  %s' % (s, member1, member2, member3)
