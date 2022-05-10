import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
weakref.ref(a,callback)
del a
del keepalive
gc.collect()
print lst

#output : ['\x00']
#python 2.6 : ['\x00']
#python 2.7 : ['\x00']
#pypy : ['\x00']

#python 2.6 : ['\x00']
#python 2.7 : ['\x00']
#pypy : ['\x00']
