import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.d=a.c
a.b=a.d.c
setattr(a,'__weakref__',callback)
keepali0e.append(a)
del a,A
#lst[0]=u'z'
#lst[0]=u'x'
#lst[0]='y'
#lst[0]=u'x'
#print(lst[0])
class int(object):pass
class bool(object):pass
while True:
	lst[0]=u'x'
	lst[0]='y'
	lst[0]=u'x'
	#lst[0]=u'x'
	#lst[0]='y'
	#lst[0]=u'x'
	d=1
	#lst[0]=u'x'
	#lst[0]='y'
	#lst[0]=u'x'
	#lst[0]=u'x'
	#lst[0]='y'
	#lst[0]=u
