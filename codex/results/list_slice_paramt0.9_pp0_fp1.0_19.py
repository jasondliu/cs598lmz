import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(a.c)

assert_raises(ReferenceError,weakref.ref,(),"")
def none_calltor(wr):pass
for cls in ['abc',123,123.456,xrange(0),object()]:weakref.ref(cls,none_calltor)
import datetime
from datetime import tzinfo
from datetime import timedelta
from datetime import datetime
ZERO=timedelta(0)
HOUR=timedelta(hours=1)
class UTC(tzinfo):
    def utcoffset(self,dt):
        return ZERO
    def tzname(self,dt):
        return 'UTC'
    def dst(self,dt):
        return ZERO
utc=UTC()
def first(iterable,default=None):
    return next(iter(iterable),default)
class CustomDelta(timedelta):
    def __new__(cls,*args,**kwargs):
        return super(CustomDelta,cls).__new__(timedelta
