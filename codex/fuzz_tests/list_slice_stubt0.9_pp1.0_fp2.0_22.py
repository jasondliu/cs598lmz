import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
dic={}
dic[a]=lst
weakref.Reference(a,callback)
"""
class Test:pass
def dic_clearer(obj):print obj,type(obj)
dic={}
test1=Test()
test2=Test()
test2.data={'abc':2}
dic['test1']=test1
dic['test2']=test2
print 'dic:',dic
weakref.ref(test1,dic_clearer)
weakref.ref(test2)
del test1
print 'dic:',dic
"""
#test2=Test()
#weakr=weakref.ref(test,dic_clearer)
#test.data={'abc':'test'}
#del test
#print weakr()
#weakref.ref(test1,dic_clearer)
#weakref.ref(test2)
#del test1
#print 'dic:',dic
