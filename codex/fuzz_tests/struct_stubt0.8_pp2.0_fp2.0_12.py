from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'HH'
s.size = s.calcsize(s.format)
values = (1, 2)
packed_data = s.pack(*values)
unpacked_data = s.unpack(packed_data)
print("""\
s = Struct.__new__(Struct)
s.format = 'HH'
s.size = s.calcsize(s.format)
values = (1, 2)
packed_data = s.pack(*values)
unpacked_data = s.unpack(packed_data)
""")
print('Format string  :', s.format)
print('Uses sys.byteorder :', s.format.startswith(sys.byteorder))
print('Size of packed structure :', s.size)
print('Values to pack:', values)
print('Packed Value   :', binascii.hexlify(packed_data))
print('Unpacked Value :', unpacked_data)
print()
print()

print("============================")
print("=   Nested Structure      =")
print("================
