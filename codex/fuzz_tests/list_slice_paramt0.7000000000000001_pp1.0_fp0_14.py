import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
del lst
del keepali0e
"""

#lst=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']*7
#print len(lst)
#for i in range(len(lst)):
#	lst[i]=str(lst[i]+str(i))
#	lst[i]=str(lst[i])
	
#print repr(lst)
#lst=[]
#for i in range(300):
#	lst.append([str(i)])
#	lst.append(str(i))
#	lst.append(str(i))
#	lst.append(str(i))
#	lst.append(str(i))
#	lst.append(str(i))
#	lst.append(str(i))
#	lst.append(str(
