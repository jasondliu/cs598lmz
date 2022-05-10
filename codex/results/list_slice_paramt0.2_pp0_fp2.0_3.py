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
#['<weakref at 0x7f5c5c0b8d70; to 'A' at 0x7f5c5c0b8d50>']

#python2.7.6
#output:
#['<weakref at 0x7f5c5c0b8d70; to 'A' at 0x7f5c5c0b8d50>']

#python3.4.3
#output:
#['<weakref at 0x7f5c5c0b8d70; to 'A' at 0x7f5c5c0b8d50>']

#python3.5.1
#output:
#['<weakref at 0x7f5c5c0b8d70; to 'A' at 0x7f5c5c0b8d50>']

#python3.
