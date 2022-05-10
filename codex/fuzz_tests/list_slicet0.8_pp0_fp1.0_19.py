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

print "I've managed to keep a single str alive"



#try:
#	gc.disable()
#except AttributeError:
#	pass
#if not hasattr(gc,"isenabled"):
#	print "I've managed to overwrite gc.isenabled"

#os._exit()
#print "I've managed to overwrite os.exit"
