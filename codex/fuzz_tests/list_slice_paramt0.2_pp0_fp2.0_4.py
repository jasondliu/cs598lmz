import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print lst

#output:
#['<weakref at 0x7f7e4c0f4b88; to 'A' at 0x7f7e4c0f4a28>']
#['<weakref at 0x7f7e4c0f4b88; dead>']
#['<weakref at 0x7f7e4c0f4b88; dead>']
#['<weakref at 0x7f7e4c0f4b88; dead>']
#['<weakref at 0x7f7e4c0f4b88; dead>']
#['<weakref at 0x7f7e4c0f4b88; dead>']
#['<weakref at 0x7f7e4c0f4b88; dead>']
#['<weakref at 0x7f7e4c0f4b88; dead>']
#['<weakref at 0x7f7e4c0f4b88; dead>']
#['<weakref
