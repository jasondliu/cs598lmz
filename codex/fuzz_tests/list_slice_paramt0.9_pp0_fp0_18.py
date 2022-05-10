import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback)) 
lst=[]
print(keepali0e)#[<weakref at 0x000002042FA31EA8; to 'A' at 0x000002042FA31C88>]
