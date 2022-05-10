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
print(keepali0e)

#python3.x
#[<weakref at 0x7f3f3f1b7c78; to 'A' at 0x7f3f3f1b7b00>, ['']]
#python2.7
#[<weakref at 0x7f3f3f1b7c78; to 'A' at 0x7f3f3f1b7b00>, ['']]

#python3.x
#[<weakref at 0x7f3f3f1b7c78; to 'A' at 0x7f3f3f1b7b00>, ['']]
#python2.7
#[<weakref at 0x7f3f3f1b7c78; to 'A' at 0x7f3f3f1b7b00>, ['']]

#python3.x
#[<weakref at 0x7f3f3f1b7c78; to 'A' at 0x7f3f3f1b7b00>, [''
