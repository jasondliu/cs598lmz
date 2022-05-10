import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])
 
print("length:",len(keepali0e))
keepali0e=keepali0e[-1]
for i in keepali0e:
    try:
        print(i)
    except TypeError as e:
        print(e)
    except ReferenceError as e:
        if 'A object' in str(e):
            pass
 
print(keepali0e)
