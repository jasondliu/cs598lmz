import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print lst
del a
print lst
lst.append(str())
print lst
del lst[1]
print lst

class C(object):
	def __init__(self,x):
		self.x=x
	def __call__(self):
		print self.x
c1=C(10)
c2=C(20)
c3=C(30)
d={}
d[c1]=10
d[c2]=20
d[c3]=30
print d
print len(d)

d={}
d[10]=C(10)
d[20]=C(20)
d[30]=C(30)
print d
print len(d)
print d[10]

d={}
d[10]=C(10)
d[20]=C(20)
d[30]=C(30)
print d
print len(d)
print d[10]

d={}
d[10]=C(10)
d[20]=C(20)
