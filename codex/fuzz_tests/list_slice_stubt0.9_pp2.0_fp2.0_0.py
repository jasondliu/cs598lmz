import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
lst[0]+='''
# to cause weakrefs to be over-collected, a cycle between a weaklist and
#  an object
a=A()
b=A()
a.b=b
b.a=a
lst=[[str()]]
c=A()
lst[0].append(c)
lst[0][0]+=1
def callback(x):pass
del lst[0]

# to fix the extreme over-collection by appending weakrefs to globals(),
#  the WeakList class was changed to subclass list
# in the past when you had a list of weakrefs and you cleared it, the underlying
#  list was left alive with all the dead weakrefs
# now, the underlying list is killed when it is left empty
#  this is important for lists of weakrefs
class MyWeakList(WeakList):
    pass
lst=[MyWeakList()]
a=[1,2,3]
wrefs=lst[0]
wrefs.append(a
