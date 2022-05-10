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

#The following code is an infinite loop in python < 2.6.2
#because the __del__ method of A refers to c.
#This is a little bit like the 'callback' in the above code
#because the destructor for 'a' calls the destructor for 'a.c'
#and the destructor for 'a.c' calls the destructor for 'a'
#and the destructor for 'a' calls the destructor for 'a.c'
#and the destructor for 'a.c' calls the destructor for 'a'
#etc.

#class A(object):
#    def __del__(self): self.c=None
#a=A()
#a.c=a
#del a
