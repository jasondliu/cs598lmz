import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
wr=weakref.WeakKeyDictionary([(a,a),(1,1),(lst[0],lst[0])])
wr[a]=a
wr[a]=a;wr[1]=1;wr[lst[0]]=lst[0]
print wr


#question2 for python test

from sets import Set
print Set()


#question3 for python test

class Container(object):pass

a=Container()
a.b=Container()
a.b.c=Container()
a.b.c.d=a
print len(a.__dict__)

#question4 for python test

#x=0o377   x=0b001

#question5 for python test

from sets import Set

s = Set()
d = {}
d['a'] = []
d['b'] = []
s.add(d)
d = {}
d['a'] = []
d['b'] = []
s.add(d)
print len(s)

#
