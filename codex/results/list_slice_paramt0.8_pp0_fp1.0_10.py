import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback=callback))
del a
gc.collect()
print len(lst)
gc.collect()
print len(lst)

def ref_callback(num,lst):
    print 'ref_callback to:',num
    lst.append(num)
lst=[]
obj=ObjectCreator()
ref=weakref.ref(obj,ref_callback,lst)
print 'obj:',obj
print 'ref:',ref
print 'lst:',lst
print 'deleting obj'
del obj
print 'lst:',lst
print 'obj:',ref()

#print gc.garbage

#print gc.collect()
#print gc.collect()
#print gc.garbage
#print gc.get_count()
#print gc.get_debug()
#print gc.get_objects()
#print sys.getrefcount(lst)
#print sys.getrefcount(ref)

#print sys.getrefcount(ref)
#print gc.get_referrers
