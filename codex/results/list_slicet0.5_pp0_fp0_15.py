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
print lst

#    import gc
#    l=[]
#    def cb(x):
#        print 'callback'
#        del l[0]
#    l.append(str())
#    a=A()
#    a.c=a
#    l.append(weakref.ref(a,cb))
#    del a
#    while l:
#        l.append(l[:])
#    print l
#    gc.collect()
#    print l
