from _struct import Struct
s = Struct.__new__(Struct)
s.code = '!Hcc8f'
s.size = s.calcsize(s.code)
dd = memoryview(data)

result = []
for i in range(0, len(dd), s.size):
    result.append(s.unpack(dd[i:i+s.size]))

print(result)
</code>
или, проще и правильнее, просто пользуясь  <code>s.iter_unpack</code>, как приведено в примерах для <code>Struct.iter_unpack</code>
:
<code>from _struct import Struct
s = Struct.__new__(Struct)
s.code = '!Hcc8f'
dd = memoryview(data)
print(list(s.iter_unpack(dd)))
</code>
Резул
