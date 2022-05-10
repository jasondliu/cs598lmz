import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m[:])
    print(ord(m[0]))
    m[0] = bytes(2)
    print(m[:])
    print(ord(m[0]))
    print(bytes(ord(m[0])) == m[:])
    print(hash(m[:]) == hash(bytes(ord(m[0]))))
print(bytes(ord(m[0])) == m[:])
</code>
this file would give me different result on win10 and macos:
<code>win10: python3.8.0
   $ python test.py
   b'\x01'
   1
   b'\x02'
   2
   False
   False
   False

macos: python3.7.4
   $ python test.py
   b'\x01'
   1
   b'\x02'
   2
   False
   True
   &lt;-- Look Something Wrong!!
</code>
I have no idea the reason of the different behavior of python on win10 and mac
