import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive=[a]
def test():
     print 'test'
test()
#test()
def set_interval(period,func):
    def p():
        #print 'a'
        func()
        threading.Timer(period,p).start()
    p()
set_interval(1,test)
