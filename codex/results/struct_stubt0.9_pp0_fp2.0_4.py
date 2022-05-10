from _struct import Struct
s = Struct.__new__(Struct)

info = {'time': 0.5, 'level': 0, 'id': 0}
for ch in b'@7Qh\x89\x02\x83\x80':
    s.unpack_from(ch, 0, info)
print info
# {'last': True, 'time': 0.5, 'level': 255, 'id': 2}
</code>

