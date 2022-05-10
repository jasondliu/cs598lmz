from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('<10s10s')

pack = s.pack
unpack = s.unpack
pack('Hello')

unpack('Hello')
```
#### 리스트나 튜플 시퀀스를 구조화한 바이트 문자열로 인코딩
`Struct(fmt).pack(*values)`
- fmt: 구조화 형식
- values: 리스트나 튜플 시퀀스

Unpack 예제:
```
from _struct import Struct
import binascii

s = Struct('>I2sh')
values = (1, 'spam', 3)
pack = s.pack(*values)
pack

binascii.hexlify(pack)
