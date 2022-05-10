import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
print(a)
keepali0e.append(a)
keepali0e.append(a.__reduce_ex__(3))
del a
f1stbyte(marshall.dumps(lst))
while keepali0e:pass
sys.getrefcount(lst)
x=lst[0]
print(sys.getrefcount(x),lst)
import weakref
a=weakref.ref(x,callback)
print(a)
del x;del a
while 1:pass
#The output is [<__main__.A object at 0x7f8a819e1b00>, 

#(b'A\nA\n', (sys.getsizeof(A()), {'c': <weakref at 0x7f8a816f8a20; to 'A' at 0x7f8a819e1b00>}, (A,))))
#2587 <__r
