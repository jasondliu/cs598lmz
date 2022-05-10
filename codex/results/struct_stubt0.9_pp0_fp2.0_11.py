from _struct import Struct
s = Struct.__new__(Struct)
s.format('H')
s.size
s.pack(1)
(b'\x00\x01',)
len(n)=2%
s.pack(2)
(b'\x00\x02',)
len(n)=2%
s.unpack(b'\x00\x01')
(1,)
tuple%
s.unpack(b'\x00\x02')
(2,)
tuple%

```
还可以通过数组模块实现效果

```python
import array
a = array.array('H',[4000,10,700,22222])
a.tobytes()
b'\x00\xfa`\x0a\x02\x9cn\xfa'
for x in a:print(x)
4000
10
700
22222

```

## 使用内存视图来操作二进
