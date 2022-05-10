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
print len(keepali0e)

#Pythonのメモリ使用量を測定したい
#__slots__
#tracemalloc
#内部イテレータの注意grouper
#__slots__を使う
class A(object):
    __slots__=['c']
    def __init__(self):
        self.c=A()
a=A()
del a
#tracemallocでスナップショット
import tracemalloc
tracemalloc.start()
A()
snap1=tracemalloc.take_snapshot()
del a
snap2=tracemalloc.take_snapshot()
#diff
stats=snap2.compare_to(snap1,'lineno')
for stat in stats[:5]:
    print stat
#内部イテレータの注意
for x in xrange(100):
    for y in xrange(100):
        pass
#grouper
def grouper
