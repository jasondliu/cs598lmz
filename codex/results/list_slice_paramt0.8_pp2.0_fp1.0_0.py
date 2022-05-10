import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
assert lst==[""]
try:__import__('gc').collect()
except:pass
assert lst==[]
try:
	import sys
	sys.exit(0)
except SystemExit as e:
	assert e.code==0
	exit(0)
