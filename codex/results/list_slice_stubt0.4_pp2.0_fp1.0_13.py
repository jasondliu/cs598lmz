import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
keepali0e.append(a)
lst.append(weakref.ref(a,callback))
print len(lst)
del a
print len(lst)
print lst
print keepali0e
del keepali0e
print lst
print len(lst)

#output:
#2
#1
#['', <__main__.A object at 0x0000000003C5F6D8>, <weakref at 0x0000000003C5F6A8; to 'A' at 0x0000000003C5F6D8>]
#[<__main__.A object at 0x0000000003C5F6D8>]
#['', <weakref at 0x0000000003C5F6A8; dead>]
#2
#
#这个例子中，第一个元素是字符串，第二个元素是一个A类的实
