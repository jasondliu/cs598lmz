import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a_wr=weakref.ref(a,callback)
print lst
del a
print lst
print "
"
xx = [1,2,3]
weakref.finalize(xx)

print "
"

me = [1]
a = [me]
me[0] = a
del a, me

##..............................................................................
# weakref.finalize(ob,func[,args[,kwargs]])
# Args:
#ob-object,指对应对象； func-callable,指对应对象被回收时，要执行的任务； args-tuple,指对应对象被回收时，func所需的参数列表；kwargs-dict,指对应对象被回收时，func
