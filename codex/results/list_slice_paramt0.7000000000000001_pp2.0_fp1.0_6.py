import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print lst
keepali0e.append(weakref.ref(a,callback))
print lst
del a
print lst
for t in xrange(10):
	tt=t
print tt
#	print t,tt
#with open('/home/user/Desktop/dns_list_2.txt') as f:
#	lines=f.readlines()
#for i in xrange(len(lines)):
#	lines[i]=lines[i].strip()
#print lines
#d=set(lines)
#print d
#if 'www.baidu.com' in d:
#	print 'yes'
#print len(lines)
#print len(d)
