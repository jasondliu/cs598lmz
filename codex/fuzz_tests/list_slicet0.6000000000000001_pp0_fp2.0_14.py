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
for i in range(len(keepali0e)):
    if i==len(keepali0e)-1:print(keepali0e[i])
    elif i==0:print(keepali0e[i])
    else:print(keepali0e[i])

#<weakref at 0x000002B0D2B7E0E8; to 'str' at 0x000002B0D2B7E1C0>
#<weakref at 0x000002B0D2B7E1C8; to 'A' at 0x000002B0D2B7E2B0>
#<weakref at 0x000002B0D2B7E1C8; to 'A' at 0x000002B0D2B7E2B0>
#<weakref at 0x000002B0D2B7E1C8; to 'A' at 0x000002B0D2B7E2B0>
#<weakref at 0x000002B0D2B7E1C8; to '
