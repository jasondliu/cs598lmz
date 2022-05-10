import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
# lst[0]='s'

lst=[]
for i in range(10):
    lst.append(i)

lst2=lst[:]
del lst[0]
print(lst)
print(lst2)
print(lst is lst2)

def test():
    print('in the test')
    return 0
lst=[1,2,3,4,5]
if test() in lst:
    print('in the list')
