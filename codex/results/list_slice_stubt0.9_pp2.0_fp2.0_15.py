import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
w=weakref.ref(a.c,callback)
lst.append(w)
	"""
	tstmod(tst,code,weakref.ref,'_A')(weakref.ref(o,c))
	
def test_reflist():
	a=[]
	b=A()
	b.l=a
	c=weakref.ref(b,lambda x: None)
	a.append(c)
	del b
	assert not c()

def test_callbacks():
	a=A()
	cbl=[]
	def cb(): cbl.append('a')
	def cb2(): cbl.append('a2')
	reflist=[]
	a.l=reflist
	ref=weakref.ref(a,cb)
	ref2=weakref.ref(a,cb2)
	reflist.append(ref)
	reflist.append(ref2)
	del a
	assert not ref()
	assert not ref2()
	assert cbl==['a','
