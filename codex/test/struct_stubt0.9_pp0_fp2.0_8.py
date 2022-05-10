from _struct import Struct
s = Struct.__new__(Struct)
s.code = '!Hcc8f'
s.size = s.calcsize(s.code)
dd = memoryview(data)

result = []
for i in range(0, len(dd), s.size):
    result.append(s.unpack(dd[i:i+s.size]))

print(result)
