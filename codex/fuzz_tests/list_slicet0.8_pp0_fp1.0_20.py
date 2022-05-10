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
print
# Test invalid methods
def callback(x):global lst;del lst[0]
lst=[str()]
w=weakref.ref(str(),callback)
try:w.validate()
except AttributeError:pass
else:print "validate() should have been invalid on a builtin reference"
try:w.acquire_lock()
except AttributeError:pass
else:print "acquire_lock() should have been invalid on a builtin reference"
try:w.release_lock()
except AttributeError:pass
else:print "release_lock() should have been invalid on a builtin reference"
try:w.releaseall()
except AttributeError:pass
else:print "releaseall() should have been invalid on a builtin reference"
print
def check_attr(name):
    try:getattr(w,name)
    except AttributeError:pass
    else:print "reference attributes",name,"shouldn't be valid on a builtin reference"
check_attr("weakreflock")
check_attr("callback")
check_attr("key")
