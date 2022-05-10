import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
keepalive.append(a)
lst.append(weakref.ref(a,callback))
del a
del lst
import gc
gc.collect()
print(keepalive)

#[<__main__.A object at 0x0000023D6E67F7C8>]
#[<__main__.A object at 0x0000023D6E67F7C8>]
#[<__main__.A object at 0x0000023D6E67F7C8>]
#[<__main__.A object at 0x0000023D6E67F7C8>]
#[<__main__.A object at 0x0000023D6E67F7C8>]
#[<__main__.A object at 0x0000023D6E67F7C8>]
#[<__main__.A object at 0x0000023D6E67F7C8>]
#[<__main__.A object at 0x0000023D6E67F7C8>]
#[<__main__
