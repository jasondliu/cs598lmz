import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a.c,callback))
del a
del keepali0e
gc.collect()
print lst

#output:
#['<weakref at 0x7f8c8c0e0c70; to 'A' at 0x7f8c8c0e0c10>']

#the weakref is not deleted

#the same code in python2.7
#output:
#[]

#the weakref is deleted

#the same code in python3.4
#output:
#[]

#the weakref is deleted
