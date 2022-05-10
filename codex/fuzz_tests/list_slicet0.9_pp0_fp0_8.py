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
print(lst)

try:a=13
except:pass
else:a=17
finally:a=19
print(a)
if not a==19:
    raise ValueError

class A(object):
    def __init__(self):self.count=0
    def __getattribute__(self,name):
         self.count+=1
         print(repr(name),self.count)
         return 3
m=A()
n=m.a+m.b
n=m.c+m.d
x=3
n=m.x+m.y
if n!=33:
    raise ValueError

a=dict(x=1,y=2,z=3,*(('magic',42),))
print(a['magic'])
b=dict(x=1,y=2,z=3,*(('magic',42),))
print(a==b)
c=dict(x=1,**a)
print(b==c)
print(a['x'])
print(c['x'
