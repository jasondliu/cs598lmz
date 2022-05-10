import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])

#MEMLEAK@NOCYTHON
#HASHING
import hashlib
hashlib.new("md5",memoryview(b'\x00'*100))

#HASHING
import hashlib
a=bytearray(b'\x00'*100)
hashlib.new("md5",memoryview(a)).digest()

#MEMLEAK@NOCYTHON
#HASHING
import hashlib
d=hashlib.new("md5")
d.update(b'ab')
d.update(b'cdef')
d.update(b'ghijkl')
d.update(b'mnopqrst')
d.update(b'uvwxyz')
d.update(b'abcdefghijklmnopqrstuvwxyz')
d.update(b'abcdefghijklmnopqrstuvwxyz')
d.update(b'abcdefghijklmnopqrstuvwxyz')
d.update(b'abcdefghijklmnop
