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
assert lst==['']
def callback(x):lst.append(x)
keepali0e=[]
lst=[]
a=A()
keepali0e.append(weakref.ref(a,callback))
b=A()
keepali0e.append(weakref.ref(b,alive_ref))
del a
try:del b
except:pass
assert lst==[a]
keepali0e=[]
lst=[]
a=A()
a.a=a
keepali0e.append(weakref.ref(a,alive_ref))
del a
keepali0e=[]
class A(object):pass
a=A()
a.a=a
r=weakref.ref(a,alive_ref)
keepali0e.append(r)
del a
for x in keepali0e:pass
assert lst==[a]
class A(object):
    def __del__(self):
        self.alive=0
    def callback(self,x):
        if not self.
