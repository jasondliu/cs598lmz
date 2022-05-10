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
lst=lst+lst
lst=keepali0e+lst
del keepali0e
keepali0e=lst[:]
lst=[]
while len(keepali0e)>2:
    lst.append(keepali0e.pop(len(keepali0e)-1))
lst=lst+lst
keepali0e.append('')
keepali0e.append('')
del lst[1:-1]
lst=[[]+lst]
lst=[[]+lst]+lst
lst=[]
keepali0e.append(lst)
keepali0e.pop()
break
keepali0e=[()]+keepali0e+keepali0e
keepali0e=lst[:]
lst=lst[:]
keepali0e.append(None)
while keepali0e:
    keepali0e.pop()
keepali0e.append('{}')
keepali0e=[repr(1.)]+keepali0e
keepali0e.append
