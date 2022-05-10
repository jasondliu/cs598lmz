import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst[0]=a
keepalive = [a,a.c]
ref = weakref.ref(a,callback)
del a
del a.c
del lst[0]
del keepalive
import gc;gc.collect()
print A()



import gc
class A(dict):
    keepalive=[]
    def __init__(self,mycallback):
        '''
        :param mycallback:
        :return:
        '''
        self.wr=weakref.ref(self,mycallback)


    def p(self):
        print 1


lst=[]
def callback(x):
    del lst[0]
a=A(callback)
print a.wr.deref()==a,a
del a
del lst[0]
import gc;gc.collect()
print A()



def f():
    def g():
        g.im_self
        yield 1


x = f().next()
print x


#detect the  classmethod
class A(object):
