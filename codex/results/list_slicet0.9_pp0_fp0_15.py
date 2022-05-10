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
del keepali0e

s=12539
while s<12600:
    if(s>0):
        s=s-3
        if s<126:
            print(s)
            continue
        else:
            s=s+3
            s=s*2
    else:s=s+4
s=s+1
print(s)


s=12539
while s<12600:
    if(s>0):
        s=s+3
        if s<12600:
            print(s)
            continue
        else:
            s=s-3
            s=s*2
    else:s=s+4
s=s+1
print(s)



s=12539
while s<12600:
    if(s>0):
        s=s+3
        if s<12600:
            continue
        else:
            s=s-3
            s=s*2
    else:s=s+4
s=s+1
print(s)

days=1

