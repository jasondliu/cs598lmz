import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a))
keepali0e.append(weakref.ref(a,callback))
del a
print(lst)
while 1:pass
# from: https://github.com/felipecruz/realpython-reader/blob/master/realpython/python2.py
# https://0x00sec.org/t/python-an-in-depth-look-at-the-memory-manager/4256
