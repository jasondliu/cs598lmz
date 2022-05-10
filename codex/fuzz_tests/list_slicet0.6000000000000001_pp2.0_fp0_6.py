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
import zlib,binascii
def gentext(length):
    import random
    t=''
    for i in range(length):
        t+=chr(random.randint(32,126))
    return t
for i in range(100):
    t=gentext(1024)
    c=zlib.compress(t)
    d=zlib.decompress(c)
    assert t==d
    c=binascii.b2a_base64(c)
    d=binascii.a2b_base64(c)
    d=zlib.decompress(d)
    assert t==d
class A(object):
    def __init__(self,a):
        self.a=a
    def __cmp__(self,other):
        return cmp(self.a,other.a)
    def __eq__(self,other):
        return self.a==other.a
    def __ne__(self,other):
        return self.a!=other.a
    def __lt__
