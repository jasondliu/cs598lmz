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
#['<__main__.A object at 0x7f8d6c2f6a90>']

#del a
#print lst

#output:
#['<__main__.A object at 0x7f8d6c2f6a90>']

#del a
#print lst

#output:
#['<__main__.A object at 0x7f8d6c2f6a90>']

#del a
#print lst

#output:
#['<__main__.A object at 0x7f8d6c2f6a90>']

#del a
#print lst

#output:
#['<__main__.A object at 0x7f8d6c2f6a90>']

#del a
#print lst

#output:
#['<__main__.A object at 0x7f8d6c2f6a90>']

#del a
#print
