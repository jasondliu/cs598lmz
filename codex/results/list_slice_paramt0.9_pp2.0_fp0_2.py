import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a.c,callback))
b=A()
b.c=b

def p():
    while 1:
        global lst
        lst=[str()]*1000
   
th=threading.Thread(target=p)
th.setDaemon(1)
th.start()

def iter_cycle(obj):
    while 1:yield weakref.ref(obj)
t=time.time()
for i in xrange(10000):
    for j in iter_cycle(a):pass
print 'single cycle: ',time.time()-t

def iter_chain(a,b):
    while 1:yield weakref.ref(a)
    
t=time.time()
for i in xrange(10000):
    for j in iter_chain(a,b):pass
print 'chain: ',time.time()-t
