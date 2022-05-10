import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
#del a
g=weakref.ref(a,callback)
callback(g)
class A(object):
    #pass
    def a_func(self):
        print 'hello'
a=A()
a_func(a)
print a.a_func
print a_func
print a.a_func is a_func
a_func.__get__(a)()
a.a_func()
a_func.__get__(None,A)()
A.a_func()
a.a_func.__get__(a)()
print a.a_func.__get__(a)()
print a.a_func.__get__(a)
#def f1(self,x,y):
#    print self,x,y
#from new import instancemethod
#ClassTypes=type(A)
#print type(instancemethod(f1,None,ClassTypes))
#print type(instancemethod(f1,None,ClassTypes)())
#print type(a.a_func)
#print type(a.a_func
