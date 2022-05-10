import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.acc=keepali0e
error=None
try:keepali0e.append(keepali0e)
except:error="cycle in keepalives"
del keepali0e
try:a.acc.append(keepali0e)
except:error="cycle in keepalives"
if error:raise ValueError,"bad starting value for keepalives -- %s"%error
a.wr=weakref.ref(a,callback)
lst=[]
del a
while callback.func_closure is not None:callback.func_closure[0].cell_contents
print"Done."
