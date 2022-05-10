import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(weakref.ref(a,callback))
del a
del keepalive[:]
print lst
print len(lst)
print lst[0]
print len(lst)

#output:
#[<weakref at 0x00A9F9B0; to 'A' at 0x00A9F8F0>, '\x00\x00\x00\x00\x00\x00\x00\x00']
#2
#<weakref at 0x00A9F9B0; dead>
#1
