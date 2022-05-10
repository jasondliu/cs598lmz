import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
try:lst[0]="1"
except:lst[0]="2"
print("ali0e")
print("ali1e")
print("ali2e")
print("ali3e")
print("ali4e")
print("ali5e")
print("ali6e")
print("ali7e")
del a
print("ali8e")
import weakref
def callback(x):del lst[0]
lst=[str()]
keepali0e=[]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
try:lst[0]="1"
except:lst[0]="2"
del a
print("ali9e")
print("aliae")
print("alibe")
print("alice")
print("alide")
print("aliee")
print("alife")
print("aliye")
print("alige")
print("alihe")
print("alije")
print("alike")
print
