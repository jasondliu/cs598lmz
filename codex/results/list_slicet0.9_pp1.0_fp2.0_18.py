import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])#绢碎走窍双钙篮山
keepali0e[0]()#绛午火海被然
print keepali0e,del keepali0e#萁礼成用鲁荐
def _(f,d={}):return lambda:f(d)
l=[_(lambda d:[d.setdefault(k,v) or v for k,v in d.iteritems()],{x:x})for x in range(100)]
print l[-1]()#口儿
print len(l[-1]())#罕类厂
print len(l[2]())#谁被窍出
print l#还止展我

#打印输出：[<weakref at 0x01D76138; dead>, ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
